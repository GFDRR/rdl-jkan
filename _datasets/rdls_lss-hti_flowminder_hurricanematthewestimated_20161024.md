---
attributions:
- entity:
    affiliation: null
    email: null
    name: Digicel
    url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Population estimates 2015
    url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016
creator:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016
dataset_id: rdls_lss-hti_flowminder_hurricanematthewestimated_20161024
description: "Summary of estimated population movement in Haiti as of 24 October 2016.\
  \ The estimated distribution of people for whom their home Section Communale in\
  \ the pre-hurricane period was in either Grande Anse, Sud or Nippes de\u0301partment,\
  \ and as of 24 October had moved to another Section Communale. Estimates are based\
  \ on movements of de-identified Digicel SIM cards which made or received at least\
  \ one call pre-hurricane and on 24 October 2016. The SIM card movements are combined\
  \ with available population data derived from estimates for the year 2015.. [Source:\
  \ This metadata record was automatically extracted from the Humanitarian Data Exchange\
  \ (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016]"
details: null
exposure: []
hazard: null
license: CC-BY-4.0
lineage:
  description: "Population displacement estimates derived from de-identified Digicel\
    \ SIM card movements (calls made or received pre-hurricane and on 24 October 2016)\
    \ in three affected d\xE9partments (Grande Anse, Sud, Nippes), scaled using 2015\
    \ population estimates to produce Section Communale-level displacement matrices."
  sources:
  - id: source_1
    license: null
    name: Digicel
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Population estimates 2015
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-24-october-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Hurricane Matthew in Haiti as of 24
      October 2016
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_strong_wind
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: strong_wind
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: displaced
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Direct Observational Data/Anecdotal Data
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Estimated population movement in Haiti based on mobile operator data
    as of 24 October 2016.
  download_url: https://data.humdata.org/dataset/4bacb766-6fe9-4240-bec5-4c5690bf317f/resource/8c54f74e-2991-4493-9370-e707591af39a/download/final_flowminder_digicel-haiti_matthew_internal-population-displacement_20161024.pdf
  format: null
  id: resource_8c54f74e
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FINAL_Flowminder_Digicel-Haiti_Matthew_Internal-Population-Displacement_20161024.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Estimated number of people away from their home Section Communale (out
    of those living pre-hurricane in Grande Anse, Sud and Nippes only). Section Communales
    are left blank where insufficient data is available.
  download_url: https://data.humdata.org/dataset/4bacb766-6fe9-4240-bec5-4c5690bf317f/resource/b745ca94-499f-4b7e-9444-bce288110149/download/hti_adm3_scaled_inflow_20161024.csv
  format: null
  id: resource_b745ca94
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_adm3_scaled_inflow_20161024.csv
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti admin level 3 shapefile, including estimated number of people
    away from their home Section Communale (out of those living pre-hurricane in Grande
    Anse, Sud and Nippes only) as of 24th October 2016.
  download_url: https://data.humdata.org/dataset/4bacb766-6fe9-4240-bec5-4c5690bf317f/resource/03ef6f38-30d4-493c-b83c-17cadf60486b/download/hti_admnbnda_adm3_cnigs2013_scaled_inflow_20161024.zip
  format: null
  id: resource_03ef6f38
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_admnbnda_adm3_CNIGS2013_scaled_inflow_20161024.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: This is the list of Section Communale included in the Port-au-Prince
    metropolitan area used for the infographic. Note that this is NOT an official
    definition of the Port-au-Prince metropolitan area.
  download_url: https://data.humdata.org/dataset/4bacb766-6fe9-4240-bec5-4c5690bf317f/resource/01918f20-dda0-44fd-8c21-40d7bcea5c69/download/pap_metro_area_pcods.csv
  format: null
  id: resource_01918f20
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pap_metro_area_pcods.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_flowminder_hurricanematthewestimated_20161024
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
  end: null
  start: '2016-10-24'
temporal_resolution: null
title: Hurricane Matthew Haiti estimated population movement as of 24 October 2016
version: null
vulnerability: null
---
