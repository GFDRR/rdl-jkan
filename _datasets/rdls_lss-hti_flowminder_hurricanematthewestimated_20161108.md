---
attributions:
- entity:
    affiliation: null
    email: null
    name: Flowminder
    url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: World Food Programme (WFP)
    url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016
creator:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016
dataset_id: rdls_lss-hti_flowminder_hurricanematthewestimated_20161108
description: "Estimated population movement in Haiti as of 8 November 2016. The estimated\
  \ distribution of people for whom their home Commune/Section Communale in the pre-hurricane\
  \ period was in either Grande Anse, Sud or Nippes de\u0301partment, and as of 8\
  \ November had moved to another Commune/Section Communale. Estimates are based on\
  \ movements of de-identified Digicel SIM cards which made or received at least one\
  \ call pre-hurricane and in the week up to 8 November 2016. The SIM card movements\
  \ are combined with available population data derived from estimates for the year\
  \ 2015.. [Source: This metadata record was automatically extracted from the Humanitarian\
  \ Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016]"
details: null
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "Population displacement was estimated by tracking de-identified Digicel\
    \ SIM card movements that made or received calls both pre-hurricane and in the\
    \ week following Hurricane Matthew (up to 8 November 2016). SIM card location\
    \ changes from three affected d\xE9partments (Grande Anse, Sud, Nippes) to other\
    \ communes were combined with 2015 population baseline estimates to derive estimated\
    \ population movement counts."
  sources:
  - id: source_1
    license: null
    name: Flowminder
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: World Food Programme (WFP)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-matthew-haiti-estimated-population-movement-as-of-8-november-2016
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population displacement from Hurricane Matthew measured via mobile
      phone SIM card movements
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
  description: "Estimated population movement in Haiti as of 8 November 2016. The\
    \ estimated distribution of people for whom their home Commune/Section Communale\
    \ in the pre-hurricane period was in either Grande Anse, Sud or Nippes de\u0301\
    partment, and as of 8 November had moved to another Commune/Section Communale.\
    \ Estimates are based on movements of de-identified Digicel SIM cards which made\
    \ or received at least one call pre-hurricane and in the week up to 8 November\
    \ 2016. The SIM card movements are combined with available population data derived\
    \ from estimates for the year 2015."
  download_url: https://data.humdata.org/dataset/f122f94e-1628-4a99-be6d-8aa6b7cdf9e1/resource/7a5c3909-1633-4d2d-9acf-de95f08b0331/download/final_hti_flowminder-wfp-population-movements-20161108.pdf
  format: null
  id: resource_7a5c3909
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FINAL_HTI_Flowminder-WFP-Population-Movements-20161108.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: 'Compressed folder containing p-coded csv files. Contains: inflow and
    outflow of people as a percentage of population at Haiti Administrative unit level
    2 and 3 (p-codes) absolute inflow and outflow of people at Haiti Administrative
    unit level 2 and 3 (p-codes) population inflow and outflow above normal at Haiti
    Administrative unit level 2 and 3 (p-codes) Summary statistics on estimated population
    flows README file containing supporting information'
  download_url: https://data.humdata.org/dataset/f122f94e-1628-4a99-be6d-8aa6b7cdf9e1/resource/66143f3a-c0d2-435e-bdfd-921427b7f498/download/flowminder-digicel-wfp_haiti-population-movement_2016-11-08.zip
  format: null
  id: resource_66143f3a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flowminder-Digicel-WFP_Haiti-population-movement_2016-11-08.zip
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_flowminder_hurricanematthewestimated_20161108
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
  start: '2016-11-08'
temporal_resolution: null
title: Hurricane Matthew Haiti estimated population movement as of 8 November 2016
version: null
vulnerability: null
---
