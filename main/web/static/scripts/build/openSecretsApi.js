var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
const apiKey = "529a9eed1fd48656f8882366bdb4d71b";
function getApiUrl() {
    return `http://www.opensecrets.org/api/?method=independentExpend&apikey=${apiKey}&output=json`;
}
function transformApiResponse(apiResponse) {
    const expenditures = [];
    for (let record of apiResponse.response.indexp) {
        const expenditure = {
            pacName: record["@attributes"].pacshort,
            supports: record["@attributes"].suppopp === "FOR:",
            candidate: record["@attributes"].candname,
            district: record["@attributes"].district,
            amount: parseInt(record["@attributes"].amount),
            note: record["@attributes"].note,
            party: record["@attributes"].party,
            payee: record["@attributes"].payee,
            date: new Date(Date.parse(record["@attributes"].date))
        };
        expenditures.push(expenditure);
    }
    return expenditures;
}
function fetchExpenditures() {
    return __awaiter(this, void 0, void 0, function* () {
        const response = yield fetch(getApiUrl());
        const rawData = yield response.json();
        return transformApiResponse(rawData);
    });
}
