var requestOptions = {
    method: 'GET',
    redirect: 'follow'
  };
  
// fetch("http://localhost:105/hello/", requestOptions)
//     .then(response => response.text())
//     .then(result => {
//         let tbody = document.getElementById("tbody");
//         result = JSON.parse(result);
//         result.data.forEach((e, i) => {
//             let fields = e.reduce((a, x) => {
//                 if (a === ``) {
//                     return a + `<td>${x}</td>`;
//                 }
//                 return a + `<td class="text-right">${x}</td>`;
//             }, ``);

//             tbody.innerHTML += `
//                 <tr>
//                     <th scope="row" class="text-right">${i}</th>
//                     ${fields}
//                 </tr>
//             `;    
//         });
//     })
//     .catch(error => console.log('error', error));

fetch("http://localhost:105/calculate", requestOptions)
    .then(response => response.text())
    .then(result => {
        let tbody2 = document.getElementById("tbody2");
        let tbody = document.getElementById("tbody");
        result = JSON.parse(result);
        console.log(result);
        let imgFuzzDCPA = document.getElementById("fuzzDCPA");
        let imgFuzzTCPA = document.getElementById("fuzzTCPA");
        let imgFuzzVCD = document.getElementById("fuzzVCD");
        let imgFuzzDr = document.getElementById("fuzzDr");

        imgFuzzDCPA.src = "Membership_DCPA.svg";
        imgFuzzTCPA.src = "Membership_TCPA.svg";
        imgFuzzVCD.src = "Membership_VCD.svg";
        imgFuzzDr.src = "Membership_Dr.svg";
        result.results.forEach((e, i) => {
            tbody2.innerHTML += `
                <tr>
                    <th scope="row" class="text-right">${i*2+1}</th>
                    <td>${result.kapals[i*2][0]}</td>
                    <td>${result.kapals[i*2][1]}</td>
                    <td>${result.kapals[i*2][2]}</td>
                    <td>${result.kapals[i*2][3]}</td>
                    <td>${result.kapals[i*2][4]}</td>
                    <td rowspan="2">${e[0]}</td>
                    <td rowspan="2">${e[3]}</td>
                    <td rowspan="2">${e[6]}</td>
                    <td rowspan="2">${e[9]}</td>
                </tr>
                <tr>
                    <th scope="row" class="text-right">${i*2+2}</th>
                    <td>${result.kapals[i*2+1][0]}</td>
                    <td>${result.kapals[i*2+1][1]}</td>
                    <td>${result.kapals[i*2+1][2]}</td>
                    <td>${result.kapals[i*2+1][3]}</td>
                    <td>${result.kapals[i*2+1][4]}</td>
                </tr>
            `  
        });
        result.results.forEach((e, i) => {
            temp = `
                <tr>
                    <th scope="row" class="text-right">${i*2+1}</th>
                    <td>${result.kapals[i*2][0]}</td>
                    `;
            for (let j = 0; j < e.length; j++) {
                temp += `<td rowspan="2">${e[j]}</td>`;
            }
            temp += `</tr>`;
            tbody.innerHTML += temp;
            tbody.innerHTML += `
                <tr>
                    <th scope="row" class="text-right">${i*2+2}</th>
                    <td>${result.kapals[i*2+1][0]}</td>
                </tr>
            `  
        });
    })
    .catch(error => console.log('error', error));