from flask import Flask, render_template, request, jsonify, session
import os
import json
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'matematik_mantik_oyunlari_2024'

# Store user progress and puzzle data
user_progress = {}
puzzle_data = {
    'game1_puzzles': [],
    'game2_puzzles': [],
    'game3_puzzles': [],
    'game4_puzzles': []
}

@app.route('/')
def index():
    """Ana sayfa"""
    return render_template('index.html')

@app.route('/game1')
def game1():
    """Niceleyici Doğruluk Oyunu"""
    return render_template('game1.html')

@app.route('/game2')
def game2():
    """Mantık Bağlaçları Bulmacası"""
    return render_template('game2.html')

@app.route('/game3')
def game3():
    """Önerme Kurma Yarışması"""
    return render_template('game3.html')

@app.route('/game4')
def game4():
    """Mantık Devresi Simülatörü"""
    return render_template('game4.html')

@app.route('/api/save_progress', methods=['POST'])
def save_progress():
    """Kullanıcı ilerlemesini kaydet"""
    try:
        data = request.get_json()
        user_id = session.get('user_id', 'anonymous')
        
        if user_id not in user_progress:
            user_progress[user_id] = {
                'game1': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                'game2': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                'game3': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                'game4': {'score': 0, 'completed': 0, 'puzzles_solved': []}
            }
        
        game = data.get('game')
        score = data.get('score', 0)
        completed = data.get('completed', 0)
        puzzle_id = data.get('puzzle_id')
        
        if game in user_progress[user_id]:
            user_progress[user_id][game]['score'] = max(user_progress[user_id][game]['score'], score)
            user_progress[user_id][game]['completed'] = max(user_progress[user_id][game]['completed'], completed)
            
            if puzzle_id and puzzle_id not in user_progress[user_id][game]['puzzles_solved']:
                user_progress[user_id][game]['puzzles_solved'].append(puzzle_id)
        
        return jsonify({'success': True, 'message': 'İlerleme kaydedildi'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get_progress')
def get_progress():
    """Kullanıcı ilerlemesini getir"""
    try:
        user_id = session.get('user_id', 'anonymous')
        progress = user_progress.get(user_id, {
            'game1': {'score': 0, 'completed': 0, 'puzzles_solved': []},
            'game2': {'score': 0, 'completed': 0, 'puzzles_solved': []},
            'game3': {'score': 0, 'completed': 0, 'puzzles_solved': []},
            'game4': {'score': 0, 'completed': 0, 'puzzles_solved': []}
        })
        return jsonify({'success': True, 'progress': progress})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get_puzzle/<game>/<int:puzzle_id>')
def get_puzzle(game, puzzle_id):
    """Belirli bir bulmacayı getir"""
    try:
        puzzles = generate_puzzles(game)
        if 0 <= puzzle_id < len(puzzles):
            return jsonify({'success': True, 'puzzle': puzzles[puzzle_id]})
        else:
            return jsonify({'success': False, 'error': 'Bulmaca bulunamadı'})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/get_daily_puzzle/<game>')
def get_daily_puzzle(game):
    """Günlük bulmaca getir"""
    try:
        # Günlük bulmaca için seed kullan
        today = datetime.now().strftime('%Y-%m-%d')
        random.seed(f"{game}_{today}")
        
        puzzles = generate_puzzles(game)
        daily_puzzle = random.choice(puzzles)
        daily_puzzle['is_daily'] = True
        daily_puzzle['date'] = today
        
        return jsonify({'success': True, 'puzzle': daily_puzzle})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/submit_puzzle_solution', methods=['POST'])
def submit_puzzle_solution():
    """Bulmaca çözümünü kontrol et"""
    try:
        data = request.get_json()
        game = data.get('game')
        puzzle_id = data.get('puzzle_id')
        user_answer = data.get('answer')
        
        puzzle = get_puzzle_by_id(game, puzzle_id)
        if not puzzle:
            return jsonify({'success': False, 'error': 'Bulmaca bulunamadı'})
        
        is_correct = check_puzzle_answer(puzzle, user_answer)
        
        # Doğruysa ilerlemeyi kaydet
        if is_correct:
            user_id = session.get('user_id', 'anonymous')
            if user_id not in user_progress:
                user_progress[user_id] = {
                    'game1': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                    'game2': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                    'game3': {'score': 0, 'completed': 0, 'puzzles_solved': []},
                    'game4': {'score': 0, 'completed': 0, 'puzzles_solved': []}
                }
            
            if puzzle_id not in user_progress[user_id][game]['puzzles_solved']:
                user_progress[user_id][game]['puzzles_solved'].append(puzzle_id)
                user_progress[user_id][game]['score'] += puzzle.get('points', 10)
        
        return jsonify({
            'success': True,
            'correct': is_correct,
            'explanation': puzzle.get('explanation', ''),
            'points': puzzle.get('points', 10) if is_correct else 0
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

def generate_puzzles(game):
    """Oyun için bulmacalar oluştur"""
    if game == 'game1':
        return [
            {
                'id': 'g1p1',
                'type': 'quantifier_puzzle',
                'title': 'Niceleyici Bulmacası 1',
                'description': 'Aşağıdaki önermenin doğruluk değerini bulun',
                'statement': '∀x ∈ {1,2,3,4,5} (x² < 30)',
                'domain': 'Küme: {1,2,3,4,5}',
                'answer': True,
                'explanation': 'Tüm elemanların karesi 30\'dan küçüktür: 1²=1, 2²=4, 3²=9, 4²=16, 5²=25',
                'points': 15,
                'difficulty': 'kolay'
            },
            {
                'id': 'g1p2',
                'type': 'quantifier_puzzle',
                'title': 'Niceleyici Bulmacası 2',
                'description': 'Bu önermenin doğruluğunu değerlendirin',
                'statement': '∃x ∈ ℕ (x + 5 = 3)',
                'domain': 'Doğal sayılar: ℕ = {1,2,3,4,...}',
                'answer': False,
                'explanation': 'x = -2 olması gerekir, ancak -2 doğal sayı değildir',
                'points': 20,
                'difficulty': 'orta'
            },
            {
                'id': 'g1p3',
                'type': 'quantifier_puzzle',
                'title': 'Niceleyici Bulmacası 3',
                'description': 'Karmaşık niceleyici önerme',
                'statement': '∀x ∈ ℝ ∃y ∈ ℝ (x + y = 0)',
                'domain': 'Gerçek sayılar: ℝ',
                'answer': True,
                'explanation': 'Her x için y = -x seçilebilir, böylece x + (-x) = 0 olur',
                'points': 25,
                'difficulty': 'zor'
            }
        ]
    elif game == 'game2':
        return [
            {
                'id': 'g2p1',
                'type': 'connective_puzzle',
                'title': 'Bağlaç Bulmacası 1',
                'description': 'Doğru bağlacı seçin',
                'statement': 'Hava güzel __ parka gideceğim',
                'options': ['∧', '∨', '→', '↔'],
                'answer': '→',
                'explanation': 'Koşullu durum için "ise (→)" bağlacı kullanılır',
                'points': 15,
                'difficulty': 'kolay'
            },
            {
                'id': 'g2p2',
                'type': 'connective_puzzle',
                'title': 'Bağlaç Bulmacası 2',
                'description': 'Karmaşık önerme tamamla',
                'statement': '(p ∧ q) __ (¬p ∨ ¬q)',
                'options': ['∧', '∨', '→', '↔'],
                'answer': '→',
                'explanation': 'Bu De Morgan yasasının bir uygulamasıdır',
                'points': 20,
                'difficulty': 'orta'
            }
        ]
    elif game == 'game3':
        return [
            {
                'id': 'g3p1',
                'type': 'builder_puzzle',
                'title': 'Önerme Kurma Bulmacası 1',
                'description': 'Verilen durumu mantıksal önerme olarak ifade edin',
                'scenario': 'Tüm öğrenciler sınavı geçmek için hem yazılı hem de sözlü sınavda başarılı olmalıdır',
                'components': ['∀', 'öğrenci', '∈', 'Sınıf', '(', 'geçer(öğrenci)', '↔', 'yazılı_başarılı(öğrenci)', '∧', 'sözlü_başarılı(öğrenci)', ')'],
                'answer': ['∀', 'öğrenci', '∈', 'Sınıf', '(', 'geçer(öğrenci)', '↔', '(', 'yazılı_başarılı(öğrenci)', '∧', 'sözlü_başarılı(öğrenci)', ')', ')'],
                'points': 25,
                'difficulty': 'orta'
            }
        ]
    elif game == 'game4':
        return [
            {
                'id': 'g4p1',
                'type': 'circuit_puzzle',
                'title': 'Devre Bulmacası 1',
                'description': 'Verilen doğruluk tablosunu sağlayan devreyi oluşturun',
                'truth_table': [
                    {'A': 0, 'B': 0, 'Output': 1},
                    {'A': 0, 'B': 1, 'Output': 1},
                    {'A': 1, 'B': 0, 'Output': 1},
                    {'A': 1, 'B': 1, 'Output': 0}
                ],
                'answer': 'NAND',
                'explanation': 'Bu NAND kapısının doğruluk tablosudur',
                'points': 20,
                'difficulty': 'orta'
            }
        ]
    
    return []

def get_puzzle_by_id(game, puzzle_id):
    """ID ile bulmaca getir"""
    puzzles = generate_puzzles(game)
    for puzzle in puzzles:
        if puzzle['id'] == puzzle_id:
            return puzzle
    return None

def check_puzzle_answer(puzzle, user_answer):
    """Bulmaca cevabını kontrol et"""
    if puzzle['type'] == 'quantifier_puzzle':
        return puzzle['answer'] == user_answer
    elif puzzle['type'] == 'connective_puzzle':
        return puzzle['answer'] == user_answer
    elif puzzle['type'] == 'builder_puzzle':
        return puzzle['answer'] == user_answer
    elif puzzle['type'] == 'circuit_puzzle':
        return puzzle['answer'] == user_answer
    return False

@app.route('/api/leaderboard')
def get_leaderboard():
    """Lider tablosu getir"""
    try:
        leaderboard = []
        for user_id, progress in user_progress.items():
            total_score = sum(game_data['score'] for game_data in progress.values())
            total_puzzles = sum(len(game_data['puzzles_solved']) for game_data in progress.values())
            
            leaderboard.append({
                'user_id': user_id,
                'total_score': total_score,
                'total_puzzles': total_puzzles,
                'games_completed': sum(1 for game_data in progress.values() if game_data['completed'] > 0)
            })
        
        # Puana göre sırala
        leaderboard.sort(key=lambda x: x['total_score'], reverse=True)
        
        return jsonify({'success': True, 'leaderboard': leaderboard[:10]})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/set_user_id', methods=['POST'])
def set_user_id():
    """Kullanıcı ID'si ayarla"""
    try:
        data = request.get_json()
        user_id = data.get('user_id', f'user_{random.randint(1000, 9999)}')
        session['user_id'] = user_id
        return jsonify({'success': True, 'user_id': user_id})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Railway deployment için port ayarı
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
