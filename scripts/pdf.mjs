import fs from 'fs';
import markdownpdf from "markdown-pdf";
import split from "markdown-pdf";
import through from "markdown-pdf";
import duplexer from "markdown-pdf";

fs.readFile('./pdf_info.json', 'utf8', function(err, data){
  const pdf_info = JSON.parse(data);
  var mdDocs = pdf_info["mdDocs"]
  console.log(mdDocs)
  var bookPath = "../airandsteel_static_site.pdf"
  var markdownOptions = {
    preProcessMd : () => {
      // Split the input stream by lines
      var splitter = split()

      // Replace occurences of "foo" with "bar"
      var replacer = through(function (data) {
        this.queue(data.replace(/EOF/g, "test??") + "\n")
      })

      splitter.pipe(replacer)
      return duplexer(splitter, replacer)
    }
  }

  markdownpdf().concat.from(mdDocs).to(bookPath, function () {
    console.log("Created", bookPath)
  })
});
// var mdDocs = [ "../posts/on-marx.mdx", "../posts/on-engels.mdx", "../posts/on-lenin.mdx", "../posts/on-stalin.mdx", "../posts/on-mao.mdx", "../posts/on-che.mdx", "../posts/on-sankara.mdx"]


