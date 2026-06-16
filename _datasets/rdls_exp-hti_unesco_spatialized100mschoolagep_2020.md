---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: IIEP-UNESCO
    url: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: UNESCO
  url: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex
creator:
  affiliation: null
  email: null
  name: UNESCO
  url: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex
dataset_id: rdls_exp-hti_unesco_spatialized100mschoolagep_2020
description: 'This GeoTIFF file contains 12 bands presenting the school age population
  for Haiti in 2020. It was constructed using constrained UN-adjusted spatialized
  age and sex population estimates for 2020 by WorldPop , by applying the methodology
  published by IIEP-UNESCO (2021). The bands contain information for Female, Male,
  and Total, for Pre-primary, Primary, Lower Secondary, and Upper secondary, reconstructed
  from single years of age using ISCED information on starting age and duration included
  in UIS . The correspondence is included below: Band 1: Pre-primary Female Band 2:
  Pre-primary Male Band 3: Pre-primary Total Band 4: Primary Female Band 5: Primary
  Male Band 6: Primary Total Band 7: Lower secondary Female Band 8: Lower secondary
  Male Band 9: Lower secondary Total Band 10: Upper secondary Female Band 11: Upper
  secondary Male Band 12: Upper secondary Total The boundaries used for the clipping
  of the resulting calculations came from the United Nations Second Administrative
  Level Boundary program . Disclaimer: The designations employed and the presentation
  of the material in this publication do not imply the expression of any opinion whatsoever
  on the part of UNESCO or IIEP concerning the legal status of any country, territory,
  city or area, or of its authorities, or concerning the delimitation of its frontiers
  or boundaries. UNESCO or IIEP are not responsible for the use given to this information..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex]'
details: null
exposure:
- asset_type:
    description: School-age population (by educational level and sex) spatially distributed
      at 100m resolution for Haiti in 2020
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
hazard: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: WorldPop 100m age-sex population estimates for Haiti 2020 were disaggregated
    from 5-year age groups to single years of age using Sprague multipliers, then
    reaggregated into school-age groups by educational level and sex following IIEP-UNESCO
    methodology (2021). The resulting 12-band GeoTIFF provides spatially explicit
    school-age population distributions at 100m resolution for disaster risk exposure
    assessment.
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
  - id: source_2
    license: null
    name: IIEP-UNESCO
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/spatialized-100m-school-age-population-grid-for-haiti-by-educational-level-and-sex
  rel: source
loss:
  losses: []
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
  description: Spatialized 100m school age population grid for Haiti, by educational
    level and sex, 2020
  download_url: https://data.humdata.org/dataset/51c17162-3920-4d89-be9f-bbaf34ba42bc/resource/adb8c71d-1d51-4456-8d17-87171976634a/download/haiti-school-age-population.tif
  format: null
  id: resource_adb8c71d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: school-age-population-haiti
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-hti_unesco_spatialized100mschoolagep_2020
spatial:
  bbox: null
  centroid: null
  countries:
  - HTI
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2020-01-01'
temporal_resolution: null
title: Spatialized 100m school age population grid for Haiti, by educational level
  and sex, 2020
version: null
vulnerability: null
---
