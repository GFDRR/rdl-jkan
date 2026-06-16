---
attributions:
- entity:
    affiliation: null
    email: null
    name: Environment Statistics of Nepal, 2013
    url: https://data.humdata.org/dataset/district-wise-population-land-ratio-and-population-density-2011
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/district-wise-population-land-ratio-and-population-density-2011
creator:
  affiliation: null
  email: null
  name: OpenNepal (inactive)
  url: https://data.humdata.org/dataset/district-wise-population-land-ratio-and-population-density-2011
dataset_id: rdls_exp-npl_opennepal_districtwisepopulationlan_20140723
description: 'The dataset consists of district wise geographical area, holding number,
  holding area, household number, population, population land ratio and poulation
  density for 2011. The data is extracted from Environment Statistics of Nepal, 2013.
  ( http://cbs.gov.np/wp-content/uploads/2014/07/Environment%20Statistics%20...).
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/district-wise-population-land-ratio-and-population-density-2011]'
details: null
exposure:
- asset_type:
    description: District-level population counts from 2011 census
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
- asset_type:
    description: District-level geographical area and land statistics
    id: natural_environment
    scheme: null
    title: null
    uri: null
  category: natural_environment
  id: exposure_2
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: ODbL-1.0/
lineage:
  description: District-level population and land statistics extracted from Nepal's
    2011 census as published in the Environment Statistics of Nepal 2013 report by
    the Central Bureau of Statistics. Data includes geographical area, household counts,
    population figures, and derived metrics (population density and population-land
    ratio) aggregated at the district administrative level.
  sources:
  - id: source_1
    license: null
    name: Environment Statistics of Nepal, 2013
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/district-wise-population-land-ratio-and-population-density-2011
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Nepal - District wise Population Land Ratio and Population Density
    (2011) (District%20wise%20Population%20Land%20Ratio%20and%20Population%20Density_0.csv)
  download_url: http://data.opennepal.net/sites/all/modules/pubdlcnt/pubdlcnt.php?file=http://data.opennepal.net/sites/default/files/resources/District%20wise%20Population%20Land%20Ratio%20and%20Population%20Density_0.csv&nid=4159
  format: null
  id: resource_2125b04d
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: District%20wise%20Population%20Land%20Ratio%20and%20Population%20Density_0.csv
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-npl_opennepal_districtwisepopulationlan_20140723
spatial:
  bbox: null
  centroid: null
  countries:
  - NPL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-07-23'
temporal_resolution: null
title: Nepal - District wise Population Land Ratio and Population Density (2011)
version: null
vulnerability: null
---
