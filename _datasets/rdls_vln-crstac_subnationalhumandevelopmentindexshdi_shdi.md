---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Global Data Lab
  url: https://globaldatalab.org/shdi/
creator:
  affiliation: null
  email: null
  name: Global Data Lab
  url: https://globaldatalab.org/shdi/
dataset_id: rdls_vln-crstac_subnationalhumandevelopmentindexshdi_shdi
description: 'The subnational Human Development Index (SHDI) is calculated from three
  dimensions: education, health and standard of living. All indicators used for the
  SHDI calculations are available, including sex-disaggregated data on expected years
  of schooling, mean years of schooling, life expectancy, and gross national income
  (GNI) per capita [Source: This metadata record was automatically extracted from
  the STAC catalog climate-risk-stac (https://climate-risk-data.github.io/climate-risk-stac/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'The subnational Human Development Index (SHDI) is calculated from
    three dimensions: education, health and standard of living. All indicators used
    for the SHDI calculations are available, including sex-disaggregated data on expected
    years of schooling, mean years of schooling, life expectancy, and gross national
    income (GNI) per capita.'
  sources:
  - id: source_underlying_1
    license: null
    name: several data sources (see publication for further details)
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
    url: https://doi.org/10.6084/m9.figshare.c.4353632
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
  name: Global Data Lab
  url: https://globaldatalab.org/shdi/
purpose: 'free user account needed; the csv file provided needs to be joined to the
  administrative units of the Global Data Lab (GDL) for download here: https://globaldatalab.org/geos/.'
referenced_by:
- author_names: null
  date_published: null
  doi: 10.1038/sdata.2019.38
  id: ref_doi
  name: null
  url: https://doi.org/10.1038/sdata.2019.38
resources:
- access_url: https://climate-risk-data.github.io/climate-risk-stac/stac/exposure-vulnerability/population/subnational-human-development-index-shdi/shdi/shdi.json
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
  spatial_aggregation: administrative units (admin1)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Item: SHDI'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: SHDI - data file
  download_url: https://globaldatalab.org/asset/394/SHDI-SGDI-Total%207.0.csv
  format: null
  id: resource_data-file_1
  media_type: text/csv
  spatial: null
  spatial_aggregation: administrative units (admin1)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: SHDI - data file
- access_url: https://doi.org/10.1038/sdata.2019.38
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SHDI (Web reference)
  download_url: null
  format: Web reference
  id: resource_link_reference
  media_type: null
  spatial: null
  spatial_aggregation: administrative units (admin1)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Reference
- access_url: https://doi.org/10.6084/m9.figshare.c.4353632
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: SHDI (Code link)
  download_url: null
  format: Web reference
  id: resource_link_codelink
  media_type: null
  spatial: null
  spatial_aggregation: administrative units (admin1)
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Code link
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-crstac_subnationalhumandevelopmentindexshdi_shdi
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
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2021'
  start: '1990'
temporal_resolution: P1Y
title: SHDI
version: null
vulnerability: null
---
