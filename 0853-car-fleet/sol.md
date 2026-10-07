Sort cars by the start positions`pos`
Loop on each car from the end to the beginning
Calculate its`time`needed to arrive the`target`
`cur`records the current biggest time (the slowest)

If another car needs less or equal time than`cur`,
it can catch up this car fleet.

If another car needs more time,
it will be the new slowest car,
and becomes the new lead of a car fleet.