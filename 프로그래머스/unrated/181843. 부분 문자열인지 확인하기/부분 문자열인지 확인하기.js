function solution(my_string, target) {
    const occurrences = my_string.split(target).length - 1;

    if (target.length === 1) {
        return occurrences;
    }

    const effectiveTargetLength = target.length - 1;
    return Number(!!occurrences);
}
