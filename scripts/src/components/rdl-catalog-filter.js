import $ from 'jquery'
import { chain, omit, defaults } from 'lodash'

import TmplListGroupItem from '../templates/list-group-item'
import { setContent, slugify, collapseListGroup } from '../util'


function prep_catalog(catalog, params, datasetsForCatalog) {
  const catalogSlug = slugify(catalog)
  const selected = params.catalog && params.catalog === catalogSlug
  const itemParams = selected ? omit(params, 'catalog') : defaults({ catalog: catalogSlug }, params)
  return {
    title: catalog === "undefined" ? "Unknown Catalog" : catalog,
    url: '?' + $.param(itemParams),
    count: datasetsForCatalog.length,
    unfilteredCount: params.length,
    selected: selected
  }
}

export default class {
  constructor(opts) {
    const catalogs = this._catalogsWithCount(opts.datasets, opts.params)
    var consolidated = []
    catalogs.forEach(function (l) {
      const idx = consolidated.findIndex(x => x.title === l.title)
      if (idx == -1) {
        consolidated.push(l)
      } else {
        consolidated[idx].count += l.count
        consolidated[idx].unfilteredCount += l.unfilteredCount
      }
    })

    const catalogsMarkup = consolidated.sort((a, b) => {
      if (a.count > b.count) return -1;
      if (a.count < b.count) return 1;
      if (a.count === b.count) {
        const titleA = a.title.toUpperCase();
        const titleB = b.title.toUpperCase();
        if (titleA < titleB) return -1;
        if (titleA > titleB) return 1;
        return 0;
      }
    }).map(TmplListGroupItem)
    setContent(opts.el, catalogsMarkup)
    collapseListGroup(opts.el)
  }

  _catalogsWithCount(datasets, params) {
    return chain(datasets)
      .groupBy('catalog')
      .flatMap(function (datasetsForCatalog, catalog) {
        var catalogs = catalog.split(",")
        var collated = catalogs.map(c => prep_catalog(c, params, datasetsForCatalog))

        return collated
      })
      .orderBy('unfilteredCount', 'desc')
      .value()
  }
}
