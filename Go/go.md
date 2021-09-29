# Settings env

## Print

    go env

## Edit

    go env -w GONOPROXY=myurl

# Packages managing

## Download

    go get code.exaas.bosch.com/xelerator/projects/api/go-modules/mongo-wrapper

add @v1.2.8 for specific version	

## Create

	go mod init

## Solve dependencies

	go mod tidy


## Create module

	go mod init

## Load local module

In go .mod put before require

	replace module => path/to/module

Then in require

	module v1.0.0


# Syntax

## References (* and &)

[https://gist.github.com/josephspurrier/7686b139f29601c3b370](https://gist.github.com/josephspurrier/7686b139f29601c3b370)

## Strings

Unescaped raw strings

	a := "\n" // This is one character, a line break.
	b := `\n` // These are two characters, backslash followed by letter n.

## Create map (dict) of misc types

	var data map[string]interface{}  // Can be {'key': 'value', 'key2': 64}

## Create array (list) of misc types

	var data map[string]interface{}  // Can be {'key': 'value', 'key2': 64}

## Conditions

Define variable only for if scope

	if err := thisCouldFail(); err != nil { 
		log.Fatal("oh no")
	}

## Type assertions

```go

_, ok := x.(string)  // Now i can use all functions accessible to string
if !ok {
    // do something
}

```

# Misc

## Requests

**Expose gin on other port**
	
	err := router.Run(":8081")


**Call request with gin context**

	result, _ := services.HttpService.CallInternalServiceReturnsJSON(c, http.MethodGet, url, nil, 200)

**Get request body to json**

```go

var response map[string]interface{}
data, err := ioutil.ReadAll(res.Body)
if err != nil {
    return nil, err
}

err = json.Unmarshal(data, &response)
if err != nil {
    return nil, err
}

```


## GIN


## Profiling (for gin)

Add to import

	"github.com/gin-contrib/pprof"

Add to router

	pprof.Register(router)
	
**Run profiler with some profile**

	curl http://localhost:8080/debug/pprof/heap > heap.out

	curl http://localhost:8080/debug/pprof/goroutine > goroutine.out

	curl http://localhost:8080/debug/pprof/block > block.out


Display on web

	go tool pprof -http=:8081 -nodefraction=0 heap.out