---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-city-of-moro-in-sindh-province-pakis-august-18-2015
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-city-of-moro-in-sindh-province-pakis-august-18-2015
dataset_id: rdls_hl-pak_unosat_geodataoverviewfloodwater_20150818
description: 'This map illustrates satellite-detected areas of flood affected land
  on the banks of river Indus as detected by Sentinel-1 image acquired 11 August 2015
  in Sindh Province, Pakistan. In districts of Naushahro Firoz, Jamshoro, Matiari
  and Nawab Shah approximately 130,000 hectares of land have been identified as flood
  affected. It is to note that the identified areas are in close proximity to Mohenjo
  Daro, a 5000 year old UNESCO world heritage site. Due to sensor limitations, flood
  waters could be underestimated in urban areas and areas covered with vegetation.
  This analysis has not yet been validated in the field. Please send ground feedback
  to UNITAR /UNOSAT.. [Source: This metadata record was automatically extracted from
  the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-city-of-moro-in-sindh-province-pakis-august-18-2015]'
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
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts processed Sentinel-1 SAR satellite imagery acquired
    on 11 August 2015, comparing pre- and post-flood images to detect notable changes
    in surface water extent. Flood-affected areas were delineated and quantified by
    area (hectares) across four districts in Sindh Province, Pakistan, with confidence
    assessments and field validation flags recorded for quality assurance.
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
- href: https://data.humdata.org/dataset/geodata-of-overview-of-flood-waters-near-city-of-moro-in-sindh-province-pakis-august-18-2015
  rel: source
loss:
  losses:
  - asset_category: agriculture
    asset_dimension: product
    description: Approximately 130,000 hectares of flood-affected agricultural land
      identified in Sindh Province districts
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
  description: Geodata of Overview of Flood Waters Near City of Moro in Sindh Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20150723PAK/FL20150723PAK_shp.zip
  format: null
  id: resource_e0402a70
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150723PAK_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Overview of Flood Waters Near City of Moro in Sindh Province,
    Pakistan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/PK/FL20150723PAK/FL20150723PAK.gdb.zip
  format: null
  id: resource_601c32d4
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: FL20150723PAK.gdb.zip
risk_data_type:
- hazard
- loss
schema: rdls-10
slug: rdls_hl-pak_unosat_geodataoverviewfloodwater_20150818
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
  start: '2015-08-18'
temporal_resolution: null
title: Geodata of Overview of Flood Waters Near City of Moro in Sindh Province, Pakistan
version: null
vulnerability: null
---
