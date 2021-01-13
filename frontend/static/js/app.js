

document.getElementById("submit").addEventListener("click", function()
{
    console.log("submit-button-clicked")

    age=d3.select("#age").selectAll("option")
    
    console.log(age)

// from project 2 to select options from user input
//     charList = d3.select(".characteristics")
//     let selected_size
//     let options = d3.select("#size").selectAll("option")
//     options.each(function (d, i) 
//     {
//         let current_option = d3.select(this)
//         if (current_option.property("selected")) 
//         {
//             selected_size = current_option._groups[0][0].value
//         }
//     })
//     console.log(selected_size)




})