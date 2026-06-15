---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-quang-nam-province-vietnam-2718
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-quang-nam-province-vietnam-2718
dataset_id: rdls_hl-vnm_unosat_detectedsurfacewatersexte_20171108
description: 'This map illustrates the satellite-detected surface waters in Quang
  Nam Province, Vietnam, as observed from the Radarsat-2 image acquired on 07 November
  2017, following the landfall of tropical cyclone DAMREY-17 on 05 November 2017.
  The districts located in the coastal areas have been affected by the floods; especially
  the ones located in the northern coastal part of the province and more particularly
  Dien Ban, Duy Xuyen and Thang Binh districts. Even if the province of Quang Nam
  was not in the passage of the cyclone, ~ 35,000 ha were identified as flooded within
  the analyzed area (8,700 km2). It represents an increase of about 230% of the surface
  waters in the analyzed zone. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR-UNOSAT.. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-quang-nam-province-vietnam-2718]'
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
  event_sets_by_hazard_type:
    flood:
    - analysis_type: empirical
      calculation_method: observed
      event_count: 0
      events: []
      frequency_distribution: null
      hazards:
      - classification: null
        id: hazard_1
        intensity_measure: AA:km2
        process: coastal_flood
        trigger: null
        type: flood
      id: event_set_1
      occurrence_range: null
      seasonality: null
  event_sets_count: 1
license: https://creativecommons.org/licenses/by-sa/4.0/
lineage:
  description: Radarsat-2 satellite imagery acquired on 07 November 2017 (2 days post-cyclone
    landfall) was analyzed by UNOSAT through visual interpretation and multi-temporal
    comparison to detect changes in surface water extent. Flooded areas were delineated
    and quantified (35,000 ha identified) to assess the spatial impact of tropical
    cyclone DAMREY-17 in Quang Nam Province.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - loss
    type: dataset
    url: null
    used_in: loss
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-surface-waters-extent-in-quang-nam-province-vietnam-2718
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Direct flood extent and inundated area detected from satellite imagery
      following tropical cyclone
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
          quantity_kind: area
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters Extent in Quang Nam Province, Vietnam
    (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_gdb.zip
  format: Geodatabase
  id: resource_0f0f6ee1
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Surface Waters Extent in Quang Nam Province, Vietnam
    (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/VN/FL20171106VNM/FL20171106VNM_shp.zip
  format: null
  id: resource_e833524d
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20171106VNM_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-vnm_unosat_detectedsurfacewatersexte_20171108
spatial:
  bbox: null
  centroid: null
  countries:
  - VNM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-11-08'
temporal_resolution: null
title: Satellite Detected Surface Waters Extent in Quang Nam Province, Vietnam
version: null
vulnerability: null
---
