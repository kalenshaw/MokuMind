from src.mokumind import pretty_recommendation

def main():
    # Example: rushdown, flashy, beginner-friendly character suggestions
    result = pretty_recommendation(
        playstyle="rushdown",
        personality="flashy",
        experience_level="beginner",
        top_k=3,
    )
    print(result)


if __name__ == "__main__":
    main()
