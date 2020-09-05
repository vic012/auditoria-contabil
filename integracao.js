//Ultilizar para integrar o python e javascript
const Express = require('express');
const app = new Express();
const porta = 3000;

app.get('/', (req, res) => res.send('Auditor Contábil 2.0.0'));

app.listen(porta, () => console.log('O servidor está rodando em: localhost:' + porta));