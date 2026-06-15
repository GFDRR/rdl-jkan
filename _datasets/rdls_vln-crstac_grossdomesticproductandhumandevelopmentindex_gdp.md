---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Dryad
  url: https://doi.org/10.5061/dryad.dk1j0
creator:
  affiliation: null
  email: null
  name: Dryad
  url: https://doi.org/10.5061/dryad.dk1j0
dataset_id: rdls_vln-crstac_grossdomesticproductandhumandevelopmentindex_gdp
description: 'This global dataset represents the gross domestic production (GDP) of
  each grid cell. GDP is given in 2011 international US dollars. The data is derived
  from GDP per capita (PPP) which is multiplied by gridded population data HYDE 3.2
  (the years of population data not available (1991-1999) were linearly interpolated
  at grid scale based on data from years 1990 and 2000). Dataset has global extent
  at 5 arc-min resolution for the 26-year period of 1990-2015. Detail description
  is given in a linked article and metadata is provided as an attribute in the NetCDF
  file itself [Source: This metadata record was automatically extracted from the STAC
  catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC0-1.0.html
lineage:
  description: An increasing amount of high-resolution global spatial data are available,
    and used for various assessments. However, key economic and human development
    indicators are still mainly provided only at national level, and downscaled by
    users for gridded spatial analyses. Instead, it would be beneficial to adopt data
    for sub-national administrative units where available, supplemented by national
    data where necessary. To this end, we present gap-filled multiannual datasets
    in gridded form for Gross Domestic Product (GDP) and Human Development Index (HDI).
  sources:
  - id: source_underlying_1
    license: null
    name: several data sources
    risk_data_type:
    - vulnerability
    type: dataset
    url: null
    used_in: vulnerability
  - id: source_code_codelink
    license: null
    name: Code link
    risk_data_type: null
    type: model
    url: https://doi.org/10.5061/dryad.dk1j0
    used_in: null
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Dryad
  url: https://doi.org/10.5061/dryad.dk1j0
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/sdata.2018.4
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/sdata.2018.4
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/gross-domestic-product-and-human-development-index/gdp/gdp.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Item metadata record for this dataset, hosted as part of
    the climate-risk-stac catalogue. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_item
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: Gross Domestic Product and Human Development Index - GDP'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Gross Domestic Product and Human Development Index - GDP - data file
  download_url: https://doi.org/10.5061/dryad.dk1j0
  format: null
  id: resource_data-file_1
  media_type: application/x-netcdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Gross Domestic Product and Human Development Index - GDP - data file
- access_url: https://doi.org/10.1038/sdata.2018.4
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Gross Domestic Product and Human Development Index - GDP (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-crstac_grossdomesticproductandhumandevelopmentindex_gdp
spatial:
  bbox:
  - -180.0
  - -90.0
  - 180.0
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: 9259
temporal:
  central_year: null
  duration: null
  end: '2015'
  start: '1990'
temporal_resolution: P1Y
title: Gross Domestic Product and Human Development Index - GDP
version: null
vulnerability: null
---
