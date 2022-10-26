ratings_letters = {"1.0": "A", "2.0": "B", "3.0": "C", "4.0": "D", "5.0": "E"}
ratings_metrics = {
    "sqale_rating": "Maintainability",
    "reliability_rating": "Reliability",
    "security_rating": "Security",
    "security_review_rating": "Security Review"
}
ratings_intervals = {
    "sqale_rating": {
        "value": "Technical Debt Radio",
        "A": "< 5%",
        "B": "6% - 10%",
        "C": "11% - 20%",
        "D": "21% - 50%",
        "E": "> 50%",
    },
    "reliability_rating": {
        "value": "Bug",
        "A": "0",
        "B": "at least 1 minor",
        "C": "at least 1 major",
        "D": "at least 1 critical",
        "E": "at least 1 blocker",
    },
    "security_rating": {
        "value": "Vulnerabilities",
        "A": "0",
        "B": "at least 1 minor",
        "C": "at least 1 major",
        "D": "at least 1 critical",
        "E": "at least 1 blocker",
    },
    "security_review_rating": {
        "value": "Reviewed Security Hotspots",
        "A": ">= 80%",
        "B": "70% and <80%",
        "C": "50% and <70%",
        "D": "30% and <50%",
        "E": "< 30%",
    }
}
