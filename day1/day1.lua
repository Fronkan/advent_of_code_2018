-- Solve puzzel 1 
function puzzel1()
    local file = io.open("day1_data.txt")
    local freq = 0
    for line in file:lines("*number") do 
        freq = freq + line
    end
    print(freq)
    file:close()
end


function puzzel2()
    local file = io.open("day1_data.txt")
    local changes = {}
    for line in file:lines("*number") do 
        table.insert(changes, line)
    end

    local freq = 0 
    local idx = 1
    local freqs = {}
    local notFound = true
    while notFound do
        freq = freq + changes[idx]

        for i, val in ipairs(freqs) do
            if freq == val then
                notFound = false
                print(freq)
                break
                
            --elseif freq > val then
            --    table.insert( freqs, i+1, freq)
            --    break
            end
        end
        table.insert( freqs,freq)

        if idx == #changes then
            idx = 1
        else
            idx = idx + 1
        end
    end
end

puzzel1()
puzzel2()

