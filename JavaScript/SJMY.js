// Description: St. John's Marina & Yacht Club
// Author: Michael Barney
// Dates: Nov 19-29 2024

// Define program constants.

const EVEN_LOT = 80.00;
const ODD_LOT = 120.00;
const ALT_MEM = 5.00;
const PROCESS_FEE = 59.99;
const WEEK_CLEAN_FEE = 50.00;
const VID_SUR_FEE = 35.00;
const CANCEL_RATE = .60;
const MEM_STD = 75.00;
const MEM_EXE = 150.00;
const HST_RATE = .15;

// Format options for displays.

const cur2Format = new Intl.NumberFormat("en-CA", {
    style: "currency",
    currency: "CAD",
    minimumFractionDigits: "2",
    maximumFractionDigits: "2",
});


// Gather user input.

let curDate = prompt("Enter the current date (YYYY-MM-DD): ");
let siteNum = prompt("Enter the site number (1-100): ");
siteNum = parseInt(siteNum);

let memName = prompt("Enter the member name: ");
let memAdd = prompt("Enter the street address: ");
let city = prompt("Enter the city: ");
let prov = prompt("Enter the province: ");
let postCode = prompt("Enter the postal code: ");
let phoneNum = prompt("Enter the phone number: ");
let cellNum = prompt("Enter the cell number: ");

// Membership and option inputs.

let memType = "E" //prompt("Enter the membership type (S-Standard or E-Executive): ");
let numAltFF = 2 //prompt("Enter the number of alternative friends and family: ");
numAltFF = parseInt(numAltFF);
let weekClean = "Y" //prompt("Weekly cleaning fee (Y/N): ");
let vidSur = "Y" //prompt("Video surveillance fee (Y/N): ");


// Site Calculations.

let siteOption = siteNum % 2

if (siteOption == 0) {
    siteCost = EVEN_LOT
} else {
    siteCost = ODD_LOT
}

let yearSiteCost = siteCost * 12

// Option Calculations.

let weekCleanFee = 0
let weekCleanMsg = "No"
if (weekClean == "Y") {
    weekCleanFee = WEEK_CLEAN_FEE
    weekCleanMsg = "Yes"
}

let vidFee = 0
let vidSurMsg = "No"
if (vidSur == "Y") {
    vidFee = VID_SUR_FEE
    vidSurMsg = "Yes"
}

optCharge = weekCleanFee + vidFee

let memTypeFee = MEM_STD
let memTypeMsg = "Standard"
if (memType == "E") {
    memTypeFee = MEM_EXE
    memTypeMsg = "Executive"
}

// Main Calculations.

let altFamCost = numAltFF * ALT_MEM;

let siteCharge = siteCost + altFamCost;

let extraCharge = vidFee + weekCleanFee; 

let subTot = siteCharge + extraCharge

let tax = subTot * HST_RATE

let monCharge = subTot + tax

let totMonFee = memTypeFee + monCharge

let yearFee = totMonFee * 12

let monPayment = (yearFee + PROCESS_FEE) / 12

let cancelFee = yearSiteCost * CANCEL_RATE







// Display results in reciept format.

document.write("<table>");
document.write(
    "<tr><th colspan='2' class='centertext'><br/>St. John's Marina & Yacht Club <br/> Yearly Member Receipt<br/><br/></th></tr>"
);

document.write("<tr><td colspan='2' class='cust'><br/>Client Name and Address:<br/><br/><hr/>" +
      memName + 
      "<br/>" +
      memAdd +
      "<br/>" +
      city + 
      ", " +
      prov +
      " " +
      postCode +
      "<br/><br/>" +
      "Phone: " +
      phoneNum +
      " (H)" +
      "<br/>" +
      "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp" +
      cellNum +
      " (C)" + 
      "</br>" +
      "<br>" +
      "</th>"
);

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Site #:" + " " + siteNum + "</td>");
document.write("<td class = 'borderlessright'>Member type:" + " " + memTypeMsg + "</td>");
document.write("</tr>");



document.write("<tr>");
document.write("<td class = 'borderlessleft'>Alternate member:<br/>Weekly site cleaning:</br>Video surveillance:</td>");
document.write("<td class = 'borderlessright'>" + numAltFF + "</br>" + weekCleanMsg + "</br>" + vidSurMsg + "</td>" );
document.write("</tr>");


document.write("<tr>");
document.write("<td class = 'borderlessleft'>Site charges:</br>Extra charges:</td>");
document.write("<td class = 'borderlessright'>" + cur2Format.format(siteCharge) + "</br>" + cur2Format.format(extraCharge) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Subtotal:</br>Sales tax(HST):</td>");
document.write("<td class = 'borderlessright'>" + cur2Format.format(subTot) + "</br>" + cur2Format.format(tax) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Total monthly fees:</br>Monthly dues:</td>");
document.write("<td class = 'borderlessright'>" + cur2Format.format(monCharge) + "</br>" + cur2Format.format(memTypeFee) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Total monthly fees:</br>Total yearly fees:</td>");
document.write("<td class = 'borderlessright'>" + cur2Format.format(totMonFee) + "</br>" + cur2Format.format(yearFee) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Monthly payment:</td>");
document.write("<td class = 'borderlessright'>" + cur2Format.format(monPayment) + "</td>");
document.write("</tr>");

document.write("<tr>");
document.write("<td class = 'borderlessleft'>Issued:</br></br>HST Registation #:<br></br>Cancellation fee:</td>");
document.write("<td class = 'borderlessright'>" + curDate + "</br>" + "</br>" + '549-33-5849-47' + "</br>" + "</br>" + cur2Format.format(cancelFee) + "</td>");
document.write("</tr>");

document.write("<td colspan='2' class='blackbottom'</td></table>");