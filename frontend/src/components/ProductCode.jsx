
function ProductsCode({name, site, price}){ 
    return(
        
          // or <div></div> or <> </> are called fragments. functions the same
        <div>
         <h4> company_name:{name}</h4>
         <p> site_name:{site}</p>
         <p> price:{price}</p>
        </div>
    )
    
}

export default ProductsCode;