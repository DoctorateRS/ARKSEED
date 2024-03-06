def generate [tag1, tag2] {
    git diff $tag1 $tag2 | save -f ./generated.patch
}

let tag1 = (input)
let tag2 = (input)

generate tag1, tag2