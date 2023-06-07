import openai

# FINE_TUNED_MODEL = "davinci:ft-personal-2023-06-07-14-02-08"
FINE_TUNED_MODEL = "ada:ft-personal-2023-06-07-17-01-11"

prompt = """
Test if cupcakeBalances is greater than zero

Contract to be tested:

contract VendingMachine {

    address public owner;
    mapping (address => uint) public cupcakeBalances;

    constructor() {
        owner = msg.sender;
        cupcakeBalances[address(this)] = 100;
    }

    function refill(uint amount) public {
        require(msg.sender == owner, "Only the owner can refill.");
        cupcakeBalances[address(this)] += amount;
    }

    function purchase(uint amount) public payable {
        require(msg.value >= amount * 1 ether, "You must pay at least 1 ETH per cupcake");
        require(cupcakeBalances[address(this)] >= amount, "Not enough cupcakes in stock to complete this purchase");
        cupcakeBalances[address(this)] -= amount;
        cupcakeBalances[msg.sender] += amount;
    }

}

\n\n###\n\n
"""

data = openai.Completion.create(
    model=FINE_TUNED_MODEL,
    prompt=prompt,
    max_tokens=1500
)

print(data)
print(data.choices[0].text)