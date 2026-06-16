---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-south-of-urmia-lake-islamic-republic-of-iran
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-south-of-urmia-lake-islamic-republic-of-iran
dataset_id: rdls_hel-irn_unosat_islamicrepublicdetectedwa_20170419
description: 'This map illustrates the satellite-detected waters extent south of Urmia
  Lake in the county of Mahabad in West Azerbaijan province of Iran as observed from
  the Landsat-8 image acquired on 16 April 2017. Within the area of 21,000 ha covered
  by this map; 2,970 ha of lands appear to be potentially affected which corresponds
  to 13% of the analyzed area. The flooded areas appear to be mainly agricultural
  zones and about 8 km of roads seem to be potentially affected. Please note that
  some areas were cloud covered and could not be analyzed.This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  - UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-south-of-urmia-lake-islamic-republic-of-iran]'
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
    description: Agricultural land in the flooded zone south of Urmia Lake
    id: agriculture
    scheme: null
    title: null
    uri: null
  category: agriculture
  id: exposure_1
  metrics:
  - dimension: product
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type:
    description: Road network potentially affected by flooding
    id: infrastructure
    scheme: null
    title: null
    uri: null
  category: infrastructure
  id: exposure_2
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: length
      unit: null
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
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts interpreted Landsat-8 satellite imagery acquired on
    16 April 2017 over the Mahabad county area, comparing multi-temporal images to
    detect water extent changes and identify flooded zones. Flooded areas were digitized
    and quantified (2,970 ha of 21,000 ha study area), with affected agricultural
    lands and road infrastructure mapped as direct impacts of the flood event.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - hazard
    type: dataset
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-south-of-urmia-lake-islamic-republic-of-iran
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Direct agricultural land inundation from flood event
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
          quantity_kind: area
          unit: null
        metric: loss
        modelling: observed
        type: direct
      loss_approach: empirical
      loss_frequency_type: empirical
      loss_type: ground_up
  - asset_category: infrastructure
    asset_dimension: structure
    description: Direct road infrastructure affected by flooding
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_flood
      intensity_measure: wd:m
      process: null
      trigger: null
      type: flood
    id: loss_2
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Islamic Republic of Iran - Satellite Detected Water Extent at the South
    of Urmia Lake (Zipped geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20170418IRN/FL20170418IRN_gdb.zip
  format: Geodatabase
  id: resource_69294aee
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170418IRN_gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Islamic Republic of Iran - Satellite Detected Water Extent at the South
    of Urmia Lake (Zipped shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/IR/FL20170418IRN/FL20170418_SHP.zip
  format: null
  id: resource_0d694720
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20170418_SHP.zip
risk_data_type:
- hazard
- exposure
- loss
schema: rdls-10
slug: rdls_hel-irn_unosat_islamicrepublicdetectedwa_20170419
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
  start: '2017-04-19'
temporal_resolution: null
title: Islamic Republic of Iran - Satellite Detected Water Extent at the South of
  Urmia Lake
version: null
vulnerability: null
---
