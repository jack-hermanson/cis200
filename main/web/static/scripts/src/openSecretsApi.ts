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