const apiKey = "529a9eed1fd48656f8882366bdb4d71b";

function getApiUrl(): string {
    return `http://www.opensecrets.org/api/?method=independentExpend&apikey=${apiKey}&output=json`;
}

interface ApiResponse {
    response: {
        indexp: Array<{
            "@attributes": {
                pacshort: string;
                suppopp: "FOR:" | "AGAINST:";
                candname: string;
                district: string;
                amount: string;
                note: string;
                party: string;
                payee: string;
                date: string;
            }
        }>
    }
}

interface IndependentExpenditure {
    pacName: string;
    supports: boolean;
    candidate: string;
    district: string;
    amount: number;
    note: string;
    party: string;
    payee: string;
    date: Date;
}

function transformApiResponse(apiResponse: ApiResponse): IndependentExpenditure[] {
    const expenditures: IndependentExpenditure[] = [];

    for (let record of apiResponse.response.indexp) {
        const expenditure: IndependentExpenditure = {
            pacName: record["@attributes"].pacshort,
            supports: record["@attributes"].suppopp === "FOR:",
            candidate: record["@attributes"].candname,
            district: record["@attributes"].district,
            amount: parseInt(record["@attributes"].amount),
            note: record["@attributes"].note,
            party: record["@attributes"].party,
            payee: record["@attributes"].payee,
            date: new Date(Date.parse(record["@attributes"].date))
        }
        expenditures.push(expenditure);
    }

    return expenditures;
}

async function fetchExpenditures(): Promise<IndependentExpenditure[]> {
    const response = await fetch(getApiUrl());
    const rawData = await response.json() as ApiResponse;
    return transformApiResponse(rawData);
}

function getPartyColor(party: string): string {
    switch (party) {
        case "R":
            return "red";
        case "D":
            return "blue";
        default:
            return "";
    }
}

let expenditures: IndependentExpenditure[] | undefined = undefined;

(async () => {
    const tableBody = document.getElementById("expenditure-table-body");
    tableBody.innerHTML = `
        <tr>
            <td colspan="8">Loading...</td>
        </tr>
    `;

    expenditures = await fetchExpenditures();
    tableBody.innerHTML = "";
    for (let expenditure of expenditures) {
        tableBody.innerHTML += `
            <tr>
                <td>${expenditure.candidate}</td>
                <td>
                    <span class="badge bg-${getPartyColor(expenditure.party)}">
                        ${expenditure.party}
                    </span>
                </td>
                <td>${expenditure.district}</td>
                <td>${expenditure.pacName}</td>
                <td>${expenditure.payee}</td>
                <td>${expenditure.supports ? "Support" : "Oppose"}</td>
                <td>$${expenditure.amount.toLocaleString()}</td>
                <td>${expenditure.date.toLocaleDateString()}</td>
            </tr>
        `
    }
})();