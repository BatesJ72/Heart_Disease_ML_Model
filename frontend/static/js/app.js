

document.getElementById("submit").addEventListener("click", function()
{

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++ DECLARE VARIABLES
    let age = d3.select("#age").property("value")
    let sex = []
    let cp = []
    let trestbps = d3.select("#trestbps").property("value")
    let chol = d3.select("#chol").property("value")
    let fbs = []   
    let restecg = []
    let thalach = d3.select("#thalach").property("value")
    let exang = []
    let oldpeak = d3.select("#oldpeak").property("value")
    let slope = []
    let ca = []
    let thal = []

// ++++++++++++++++++++++++++++++++++++++++++++++++++++++ PULL RESULTS FOR MULTI CHOICE ENTRY


//SEX
    let sex_options = d3.select("#sex").selectAll("option")
    sex_options.each(function (d, i) 
    {
        let sex_current_option = d3.select(this)
        if (sex_current_option.property("selected")) 
        {
            sex.push(sex_current_option._groups[0][0].value)
        }
    })
    
//CP
    let cp_options = d3.select("#cp").selectAll("option")
    cp_options.each(function (d, i) 
    {
        let cp_current_option = d3.select(this)
        if (cp_current_option.property("selected")) 
    {
        cp.push(cp_current_option._groups[0][0].value)
    }
    })

//FBS
    let fbs_options = d3.select("#fbs").selectAll("option")
    fbs_options.each(function (d, i) 
    {
        let fbs_current_option = d3.select(this)
        if (fbs_current_option.property("selected")) 
        {
            fbs.push(fbs_current_option._groups[0][0].value)
        }
    })

//RESTECG
    let restecg_options = d3.select("#restecg").selectAll("option")
    restecg_options.each(function (d, i) 
    {
        let restecg_current_option = d3.select(this)
        if (restecg_current_option.property("selected")) 
    {
        restecg.push(restecg_current_option._groups[0][0].value)
    }
    })

//EXANG
    let exang_options = d3.select("#exang").selectAll("option")
    exang_options.each(function (d, i) 
    {
        let exang_current_option = d3.select(this)
        if (exang_current_option.property("selected")) 
    {
        exang.push(exang_current_option._groups[0][0].value)
    }
    })

//SLOPE
    let slope_options = d3.select("#slope").selectAll("option")
    slope_options.each(function (d, i) 
    {
        let slope_current_option = d3.select(this)
        if (slope_current_option.property("selected")) 
    {
        slope.push(slope_current_option._groups[0][0].value)
    }
    })

//CA
    let ca_options = d3.select("#ca").selectAll("option")
    ca_options.each(function (d, i) 
    {
        let ca_current_option = d3.select(this)
        if (ca_current_option.property("selected")) 
    {
        ca.push(ca_current_option._groups[0][0].value)
    }
    })

// THAL
    let thal_options = d3.select("#thal").selectAll("option")
    thal_options.each(function (d, i) 
        {
            let thal_current_option = d3.select(this)
            if (thal_current_option.property("selected")) 
        {
            thal.push(thal_current_option._groups[0][0].value)
        }
        })





// ++++++++++++++++++++++++++++++++++++++++++++++++++++++ LOG EACH RESULT


    // console.log(cp)
    // console.log(sex)
    // console.log(fbs)
    // console.log(restecg)
    // console.log(exang)
    // console.log(slope)
    // console.log(ca)
    // console.log(thal)

    console.log([age,sex,cp,fbs,trestbps,chol,restecg,thalach,exang,oldpeak,slope,ca,thal])


// ++++++++++++++++++++++++++++++++++++++++++++++++++++++ LOAD RESULTS DIV

    let resultBox = document.getElementById("result-box")
 
        if (resultBox.style.display == "none")
        {
            return resultBox.style.display = "block";
        }
        
})