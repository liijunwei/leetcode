def two_sum(given_array, target)
  given_array.each_with_index do |num, index|
    leftover_array = given_array.reject {|k| k == num }
    leftover_array.each_with_index do |leftover_num, leftover_index|
      return [index, leftover_index+1] if num + leftover_num == target
    end
  end

  return []
end

def assert(expected, actual)
  puts "pass" if expected == actual
  puts "fail" unless expected == actual
end

assert(two_sum([2, 7, 11, 15], 9 ), [0, 1])
assert(two_sum([2, 7, 11, 15], 13), [0, 2])
assert(two_sum([2, 7, 11, 15], 17), [0, 3])
assert(two_sum([2, 7, 11, 15], 18), [1, 2])
assert(two_sum([2, 7, 11, 15], 22), [1, 3])
assert(two_sum([2, 7, 11, 15], 26), [2, 3])
assert(two_sum([2, 7, 11, 15], 2 ), []    )
