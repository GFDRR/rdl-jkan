---
attributions:
- entity:
    affiliation: null
    email: null
    name: Sentinel-1 satellite imagery
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar
  id: attribution_1
  role: collaborator
- entity:
    affiliation: null
    email: null
    name: WorldPop
    url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar
  id: attribution_2
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar
dataset_id: rdls_hl-mmr_unosat_detectedwaterextentas1618_20190725
description: 'UNOSAT code: FL20190715MMR This map illustrates the cumulative satellite
  detected surface waters in Kachin, Myanmar by using a Sentinel-1 images acquired
  on 16 and 18 July 2019. Over an area of about 370 km2 of lands appear to be likely
  flooded. By using the population data from Worldpop, total of about 34,000 people
  appear to have been affected by floods as of 18 July 2019. This is preliminary analysis
  that has not yet been validated in the field. Please send your comments to UNITAR-UNOSAT..
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar]'
details: This is a preliminary assessment and has not yet been validated in the field.
  It is important to consider the characteristics of the source imagery used in the
  analyses when interpreting results. For damage assessments it should be noted that
  only significant damage to the structural integrity of the buildings analyzed can
  be seen in imagery, while minor damage such as cracks or holes may not be visible
  at all. For flood extractions using radar data it is important to note that urban
  areas and highly vegetated areas may mask the flood signature and result in underestimation
  of flood waters. Users with specific questions or concerns should contact unosat@unitar.org
  to seek clarification.
exposure: []
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
      intensity_measure: wd:m
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: "Sentinel-1 SAR imagery from 16-18 July 2019 was analyzed by UNOSAT\
    \ through multi-temporal change detection to identify surface water extent. The\
    \ resulting flood extent polygon (370 km\xC2\xB2) was intersected with WorldPop\
    \ gridded population data to estimate affected population (~34,000 people). This\
    \ is a preliminary post-event impact assessment not yet validated in the field."
  sources:
  - id: source_1
    license: null
    name: Sentinel-1 satellite imagery
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
  - id: source_2
    license: null
    name: WorldPop
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-as-of-16-and-18-july-2019-over-kachin-state-myanmar
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Population affected by satellite-detected flooding derived from WorldPop
      population data
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
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
  description: Satellite detected water extent, as of 16 and 18 July 2019 over Kachin
    state, Myanmar (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20190715MMR/FL20190715MMR_GDB.zip
  format: Geodatabase
  id: resource_861998c8
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190715MMR_GDB.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite detected water extent, as of 16 and 18 July 2019 over Kachin
    state, Myanmar (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/MM/FL20190715MMR/FL20190715MMR_SHP.zip
  format: null
  id: resource_ebfd2c99
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20190715MMR_SHP.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-mmr_unosat_detectedwaterextentas1618_20190725
spatial:
  bbox: null
  centroid: null
  countries:
  - MMR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2019-07-25'
temporal_resolution: null
title: Satellite detected water extent, as of 16 and 18 July 2019 over Kachin state,
  Myanmar
version: null
vulnerability: null
---
