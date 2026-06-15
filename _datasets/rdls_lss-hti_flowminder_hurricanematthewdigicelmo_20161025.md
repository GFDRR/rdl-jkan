---
attributions:
- entity:
    affiliation: null
    email: null
    name: Digicel Haiti
    url: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: Flowminder
    url: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016
creator:
  affiliation: null
  email: null
  name: Flowminder (inactive)
  url: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016
dataset_id: rdls_lss-hti_flowminder_hurricanematthewdigicelmo_20161025
description: 'Summary of Digicel Haiti mobile network functionality as of 25th October
  2016. Proportion of Digicel Haiti network (radio cells) with normal function per
  commune (admin level 2) as of 25th October 2016. French version provided.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016]'
details: The network recovery effort now far advanced, but still ongoing. Note that
  functioning mobile towers in an area may not always translate into the ability of
  all users to place calls as communication demands are high and network capacity
  reduced. The data does not differentiate between 2G, 3G or 4G services and therefore
  primarily serves as a guide to the functionality of voice and SMS services.
exposure: []
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: Direct observational data from Digicel Haiti mobile network infrastructure
    was collected on 25 October 2016 following Hurricane Matthew. Network functionality
    status (proportion of active radio cells) was aggregated by commune (administrative
    level 2) and spatially represented in shapefile and CSV formats.
  sources:
  - id: source_1
    license: null
    name: Digicel Haiti
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
  - id: source_2
    license: null
    name: Flowminder
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/hurricane-matthew-digicel-haiti-mobile-network-functionality-as-of-25-october-2016
  rel: source
loss:
  losses:
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct infrastructure damage to mobile network radio cells from Hurricane
      Matthew
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
        metric: loss
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
  description: Hurricane Matthew Digicel Haiti mobile network functionality as of
    25 October 2016 (Summary of Digicel Haiti mobile network functionality as of 25th
    October 2016.)
  download_url: https://data.humdata.org/dataset/82734eab-d104-4d98-8471-1905d71f51c1/resource/1a1dfdd5-c2e7-42cb-a2fc-d9cfd2d88d72/download/flowminder_digicel-haiti_matthew_network-status_20161025.pdf
  format: null
  id: resource_1a1dfdd5
  media_type: application/pdf
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Flowminder_Digicel-Haiti_Matthew_Network-Status_20161025.pdf
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Haiti admin level 2 shapefile, including proportion of Digicel Haiti
    network (radio cells) with normal function per commune (admin level 2) as of 25th
    October 2016.
  download_url: https://data.humdata.org/dataset/82734eab-d104-4d98-8471-1905d71f51c1/resource/86cafe28-bd1b-4096-8cf6-41d5f6129d0b/download/hti_admnbnda_adm2_cnigs2013_propactivesites_20161025.zip
  format: null
  id: resource_86cafe28
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: hti_admnbnda_adm2_CNIGS2013_propActiveSites_20161025.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Proportion of Digicel Haiti network (radio cells) with normal function
    per commune (admin level 2) as of 25th October 2016.
  download_url: https://data.humdata.org/dataset/82734eab-d104-4d98-8471-1905d71f51c1/resource/e21b7e3e-ac09-4ff8-89e8-3745e911a0d1/download/proportion_cells_active_adm2_matthew_20161025.csv
  format: null
  id: resource_e21b7e3e
  media_type: text/csv
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: proportion_cells_active_adm2_Matthew_20161025.csv
risk_data_type:
- loss
schema: rdls-10
slug: rdls_lss-hti_flowminder_hurricanematthewdigicelmo_20161025
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
  start: '2016-10-25'
temporal_resolution: null
title: Hurricane Matthew Digicel Haiti mobile network functionality as of 25 October
  2016
version: null
vulnerability: null
---
