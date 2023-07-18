const {PythonShell} =require('python-shell');
const express=require('express')
const upload=require('express-fileupload')
const app=express()

app.set('view engine','ejs')
const path = require("path")
const content_path = path.join(__dirname, "static")
app.use(express.static(content_path))
app.use(upload())

app.get('/',function(req,res){
    res.render('index')   
})

app.post('/addpic',async function(req,res){
    if(req.files){
        console.log(req.files)
    }

    var file=req.files.file
    var filename=file.name

    file.mv('./uploads/'+filename,function(err){
        if(err){
            res.send(err)
        }
        else{
            
        }
    })

    var destination='./uploads/'+filename
    
    let options={
        args:[destination]
    }

    await PythonShell.run('app.py', options).then(messages=>{
            // results is an array consisting of messages collected during execution
            console.log(messages);
    });
    
    res.render('showpic')
})

app.listen(3000, () => {
    console.log('Server started on port 3000');
});

