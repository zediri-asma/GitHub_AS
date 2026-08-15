import os

from openai import OpenAI


def main() -> None:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "Missing OPENAI_API_KEY. Set it in your environment before running this script."
        )

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a short greeting in 2 sentences."},
        ],
        temperature=0.7,
    )

    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
