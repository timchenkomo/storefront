// Sample : /sample/{product_slug}.{ext} : {product_slug}/sample.{ext}
// Product: /{product_slug}.{ext}        : {product_slug}/{product_slug}.{ext}
// Reader : /{product_slug}.epub         : {product_slug}/{product_slug}.epub

export function getSampleUrl(slug: string, ext: string) {
  return process.env.baseUrlApiBrowser + '/api/download/' + slug + '/sample.' + ext
}

export function getProductUrl(slug: string, ext: string) {
  return process.env.baseUrlApiBrowser + '/api/download/' + slug + '.' + ext
}

export function getReaderUrl(slug: string) {
  // reader supports epub format only
  return getSampleUrl(slug, 'epub')
}
