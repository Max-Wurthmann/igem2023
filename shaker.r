#!/bin/Rscript
# This script facilitates the control of BioShake microtiter plate shakers directly from a computer. 

packages <- c("optparse", "serial")

install.packages(setdiff(packages, rownames(installed.packages())))
suppressPackageStartupMessages({
library(optparse)
library(serial)
})

optionList <- list(make_option(c("-v", "--verbose"), action = "store_true",
																default = FALSE, help = "Print extra output [default]"),
make_option(c("-s", "--shake"), action = "store", help = "Start shaking at X rpm. Use X = 0 to stop shaking."),
make_option(c("-o", "--open"), action = "store_true", default = FALSE, help = "Open the thing"),
make_option(c("-c", "--close"), action = "store_true", help = "Close the thing", default = FALSE),
make_option(c("-t", "--temperature"), action = "store", help = "Heat the plate to the temperature X. Set to 0 to turn off the temperature control"),
make_option(c("-p", "--port"), action = "store", default = "ttyUSB0"))

opt <- parse_args(OptionParser(option_list = optionList,
															 usage = "usage: %prog [sequences.fasta]")
)

con <- serialConnection(name = "testcon",port = "ttyUSB0"
												,mode = "9600,n,8,1"
												,newline = 1)

open(con)

Sys.sleep(1)
read.serialConnection(con)

if (opt$open && opt$close) {
	stop("you cannot open and close the shaker in one command, use -o OR -c")
} else if (opt$open) {
	write.serialConnection(con, "setElmUnlockPos\r")
	Sys.sleep(1)
	out = read.serialConnection(con)
	print(ifelse(out == "ok", "Open position", "ERROR!"))
	if(opt$verbose) {
		print(out)
	}
} else if (opt$close) {
	write.serialConnection(con, "setElmLockPos\r")
	Sys.sleep(1)
	out = read.serialConnection(con)
	print(ifelse(out == "ok", "Closed position", "ERROR!"))
	if(opt$verbose) {
		print(out)
	}
}

if (!is.null(opt$shake)) {
	if (opt$shake == 0) {
		write.serialConnection(con, "'soff\r")
		print("Stopped shaking")
		Sys.sleep(1)
		print(read.serialConnection(con))
	} else {
		write.serialConnection(con, paste("ssts", opt$shake, "\r", sep = ""))
		print(paste("ssts", opt$shake, "\r", sep = ""))
		write.serialConnection(con, "'son\r")
	}
	if(opt$verbose) {
		print(out)
	}
}

if (!is.null(opt$temperature)) {
	if (opt$temperature == 0) {
		write.serialConnection(con, "'tempOn\r")
		print("Temperature controll off")
		Sys.sleep(1)
		if(opt$verbose) {
			print(read.serialConnection(con))
		}
	} else {
		write.serialConnection(con, paste("stt", opt$shake, "\r", sep = ""))
		write.serialConnection(con, "'ton\r")
	}
	if(opt$verbose) {
		print(out)
	}
}

close(con)
