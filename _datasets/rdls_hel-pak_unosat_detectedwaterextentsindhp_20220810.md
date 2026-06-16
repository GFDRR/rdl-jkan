---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 SAR imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022
dataset_id: rdls_hel-pak_unosat_detectedwaterextentsindhp_20220810
description: 'UNOSAT code: FL20220808PAK This map illustrates satellite-detected surface
  waters in Satellite detected water in Sindh province, Pakistan as observed from
  a Sentinel-1 image acquired on 06 August 2022 at 06:25 local time. Within the analyzed
  area of about 59,000 km2, about 2,700 km2 of lands appear to be flooded. Based on
  Worldpop population data and the detected surface waters in the analyzed area, about
  750,000 are potentially exposed or living close to flooded areas. This is a preliminary
  analysis and has not yet been validated in the field. Please send ground feedback
  to United Nations Satellite Centre (UNOSAT).. [Source: This metadata record was
  automatically extracted from the Humanitarian Data Exchange (HDX); Original dataset:
  https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022]'
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
    description: Population potentially exposed or living close to flooded areas,
      derived from WorldPop data intersected with detected water extent
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
  description: "Sentinel-1 SAR imagery from 06 August 2022 was analyzed by UNOSAT\
    \ through visual interpretation and change detection to identify surface water\
    \ extent in Sindh province. The detected water polygons (2,700 km\xC2\xB2) were\
    \ intersected with WorldPop gridded population data to estimate approximately\
    \ 750,000 people potentially exposed to flooding. This is a preliminary post-event\
    \ assessment not yet validated in the field."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 SAR imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-sindh-province-pakistan-as-of-06-august-2022
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population potentially exposed to fluvial flooding based on satellite-detected
      inundation extent
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
  description: Satellite detected water extent in Sindh province, Pakistan, as of
    06 August 2022 (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_gdb.zip
  format: Geodatabase
  id: resource_0ffaff6d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent in Sindh province, Pakistan, as of
    06 August 2022 (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/PK/FL20220808PAK/FL20220808PAK_SHP.zip
  format: null
  id: resource_03a0da8a
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20220808PAK_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-pak_unosat_detectedwaterextentsindhp_20220810
spatial:
  bbox: null
  centroid: null
  countries:
  - PAK
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2022-08-10'
temporal_resolution: null
title: Satellite detected water extent in Sindh province, Pakistan, as of 06 August
  2022
version: null
vulnerability: null
---
