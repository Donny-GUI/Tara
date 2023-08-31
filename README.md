# Tara ✨
Type And Return Automater

## Description
Automate python type hints for params and return values

## Getting Started

#### Windows
```Powershell
git clone https://github.com/Donny-GUI/Tara.git
python add_type_hints.py <yourfile>
```
#### Linux
```Bash
git clone https://github.com/Donny-GUI/Tara.git
python3 add_type_hints.py <yourfile>
```


# BEFORE 📷
![before](https://github.com/Donny-GUI/variable_type_hint_writer/assets/108424001/de9d19c6-e5b5-4b6f-9917-d930860a9052)

# AFTER 📸
![after](https://github.com/Donny-GUI/variable_type_hint_writer/assets/108424001/5207c1e5-3114-4d5f-99e3-239cbe091b36)
![after](https://github.com/Donny-GUI/variable_type_hint_writer/assets/108424001/dc97553a-e715-44cf-a013-1c6b44501535)



## How?
Parameters use a mix of symbolic execution, natural language processing and static analysis. Then finally a large language model to find a reasonable type if none is assigned.

For Return Types
1. Determine if the function has a return ast
2. Find those statements that push return
3. Check if it has a type hint or type annotation
4. Analyize the literal string of the return value for lexigraphical hints
5. if no result, use language syntax to infer type.
6. Reanalyze to make sure the type or types makes sense

## To Come 
1. Secondary Types - Genrators/iters, slices, Callable, Array, etc
2. Standard Library Types - Index the standard library return types and objects. build a map to function -> return object

