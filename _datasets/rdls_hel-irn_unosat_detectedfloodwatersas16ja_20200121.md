---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-2 satellite imagery
    url: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop population data
    url: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir
dataset_id: rdls_hel-irn_unosat_detectedfloodwatersas16ja_20200121
description: 'UNOSAT code: FL20200117IRN This map illustrates satellite-detected waters
  in Dalgan County, Sistan and Baluchestan Province, Islamic Republic of Iran, as
  observed from Sentinel-2 imagery acquired on 16 January 2020. Within the analysed
  area of 2,130 km2, a total of 647 km2 of land appear to be flooded in Dalgan County.
  Based on Worldpop population data and the detected surface waters, about 2,500 people
  are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to UNITAR -UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure:
- asset_type:
    description: Population potentially exposed or living close to detected flooded
      areas based on WorldPop data
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
hazard:
  event_sets:
  - analysis_type: empirical
    calculation_method: observed
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: "UNOSAT analysts reviewed Sentinel-2 satellite imagery acquired on\
    \ 16 January 2020 and performed visual change detection to identify surface water\
    \ extent in Dalgan County. Detected flood waters (647 km\xB2 within 2,130 km\xB2\
    \ analysis area) were intersected with WorldPop population data to estimate approximately\
    \ 2,500 people potentially exposed to flooded areas. This is a preliminary post-event\
    \ assessment not yet validated in the field."
  sources:
  - id: source_1
    license: null
    name: Sentinel-2 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop population data
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/flood-waters-as-of-16-january-2020-over-golmorti-sistan-and-baluchestan-province-i-r-of-ir
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population exposed to satellite-detected flood waters in Dalgan County
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: AA:km2
      process: null
      trigger: null
      type: flood
    id: loss_1
    impact_and_losses:
      impact:
        measurement:
          quantity_kind: count
          unit: null
        metric: exposure
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected flood waters, as of 16 January 2020, over Golmorti,
    Sistan and Baluchestan Province, I. R. of Iran (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20200117IRN/FL20200117IRN_gdb.zip
  format: Geodatabase
  id: resource_6648b01e
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200117IRN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite-detected flood waters, as of 16 January 2020, over Golmorti,
    Sistan and Baluchestan Province, I. R. of Iran (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20200117IRN/FL20200117IRN_SHP.zip
  format: null
  id: resource_3dc1858c
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20200117IRN_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-irn_unosat_detectedfloodwatersas16ja_20200121
spatial:
  bbox: null
  centroid: null
  countries:
  - IRN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-01-21'
temporal_resolution: null
title: Satellite-detected flood waters, as of 16 January 2020, over Golmorti, Sistan
  and Baluchestan Province, I. R. of Iran
version: null
vulnerability: null
---
