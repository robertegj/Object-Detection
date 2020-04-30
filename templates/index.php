<html>
  <head>
    <title>Anicyber Video Analytics</title>
    <style>
        body {
            font-family: Calibri;
            background-color: #222;
        }
        h1 {
            padding: 1em;
            color: white;
            display: inline-block;
        }
        #livePlayer {
            text-align: center;
            background-color: white;
            border: 1px solid #fe525b;
            display: inline-block;
            float: right;
        }
        .btn {
            display: inline-block;
            border: .2em solid #fe525b;
            box-shadow: 2px 4px 3px #666;
            border-radius: .5em;
            padding: .5em;
            margin: 1em;
            font-size: 1em;
            background-color: rgba(0,0,0,0);
        }
        .btn:hover {
            border: .2em solid #fe525b;
            background-color: #fe525b;
        }
        a {
            text-decoration: none;
            color: black;
        }
        nav {
            border-bottom: 1px solid white;
        }
        nav > .btn {
            display: inline-block;
            float: right;
            color: white;
            margin: 2em;
            box-shadow: 2px 4px 3px #000;
        }
    </style>
  </head>
  <body>
      <nav>
          <h1><font color="#fe525b">Anicyber</font> Video Analytics</h1>
          <a class="btn" href="">REFRESH</a>
      </nav>
      <br>
      <div id="livePlayer">
        <h2>Live Player </h2>
          
        <img id="bg" src="{{ url_for('video_feed') }}">
          
        <p>streaming from: {{ url_for('video_feed') }}</p>
        
        <a class="btn" href="/stop">stop</a>
        <a class="btn" href="">start</a>
      </div>
  </body>
</html>