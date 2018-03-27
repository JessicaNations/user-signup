from flask import Flask, request, redirect
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

page_header = """
<!DOCTYPE html>
<html>
    <head>
     <style>
      .error {
          color:red;
      }
     </style>
    </head>
    <body>
    <h1>Signup</h1>
"""
page_footer = """
    </body>
</html>
"""
form = """
      <form method="port">
        <table>
          <tr>
            <td><label for="username">Username</label>
</td>
            <td>
              <input name="username" type="text" value="">
              <span class="eror"></span>
            </td>
          </tr>
          <tr>
            <td><label for="password">Password</label></td>
            <td>
              <input name="password" type="password">
              <span class="error"></span>
            </td>
          </tr>
          <tr>
            <td><labe for="verify">Verify Password</label>
</td>
            <td>
              <input name="verify" type="password">
              <span class="error"></span>
            </td>
          </tr>
          <tr>
            <td><label for="email">Email (optional)</label>
</td>
            <td>
              <input name="email" value="">
              <span class="error"></span>
            </td>
          </tr>
        </table>
        <input type="submit">
      </form>
"""

@app.route("/")
def index():
    content = page_header + "<p>" + form + "</p>" + page_footer 
    return content
    
app.run() 
