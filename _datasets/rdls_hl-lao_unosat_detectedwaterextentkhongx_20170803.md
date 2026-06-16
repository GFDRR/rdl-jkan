---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-khongxedone-district-salavan-province-lao-pdr
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/satellite-detected-water-extent-in-khongxedone-district-salavan-province-lao-pdr
dataset_id: rdls_hl-lao_unosat_detectedwaterextentkhongx_20170803
description: 'This map illustrates the satellite-detected water extent in the District
  of Khongxedone, Salavan Province, in the southwestern part of Lao People''s Democratic
  Republic after the tropical storm SONCA-17. The UNITAR-UNOSAT analysis used a Sentinel-1
  satellite image acquired on the 30 July 2017 and detected several areas with potentially
  standing waters. In the district of Khongxedone ~2,921 ha are likely flooded mostly
  affecting the central part of the district along the ''Xe Don'' river. This is a
  preliminary analysis and has not yet been validated in the field. Please send ground
  feedback to UNITAR-UNOSAT.. [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/satellite-detected-water-extent-in-khongxedone-district-salavan-province-lao-pdr]'
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
      intensity_measure: AA:km2
      process: fluvial_flood
      trigger: null
      type: flood
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-SA-4.0
lineage:
  description: UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired
    on 30 July 2017 following tropical storm SONCA-17, comparing pre- and post-event
    images to detect notable changes in water extent. Standing water areas were delineated
    and quantified (2,921 ha) in vector format (geodatabase and shapefile) with spatial
    and temporal metadata. This is a preliminary post-event damage assessment not
    yet validated in the field.
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
- href: https://data.humdata.org/dataset/satellite-detected-water-extent-in-khongxedone-district-salavan-province-lao-pdr
  rel: source
loss:
  losses:
  - asset_category: natural_environment
    asset_dimension: product
    description: Post-event satellite-detected flooded area extent following tropical
      storm SONCA-17
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
  description: Satellite Detected Water Extent in Khongxedone District, Salavan Province,
    Lao PDR (Zipped geodatabase)
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO.gdb.zip
  format: Geodatabase
  id: resource_5accb044
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO.gdb.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Satellite Detected Water Extent in Khongxedone District, Salavan Province,
    Lao PDR (Zipped shapefile)
  download_url: https://cern.ch/unosat-maps/LA/TC20170731LAO/TC20170731LAO_shp.zip
  format: null
  id: resource_b064100e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: TC20170731LAO_shp.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-lao_unosat_detectedwaterextentkhongx_20170803
spatial:
  bbox: null
  centroid: null
  countries:
  - LAO
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2017-08-03'
temporal_resolution: null
title: Satellite Detected Water Extent in Khongxedone District, Salavan Province,
  Lao PDR
version: null
vulnerability: null
---
