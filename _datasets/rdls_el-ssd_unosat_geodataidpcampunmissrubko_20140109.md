---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-rubkona-base-rubkona-south-sudan-january-09-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-rubkona-base-rubkona-south-sudan-january-09-2014
dataset_id: rdls_el-ssd_unosat_geodataidpcampunmissrubko_20140109
description: 'This map illustrates satellite-detected areas of IDPs in the UNMISS
  Rubkona base as seen by the WorldView-2 satellite on 2 January 2014. Fleeing outbreaks
  of violence, a portion of the UNMISS compound was in use by IDPs, occupying more
  than 2.6 ha. Note that IDP occupied areas include improvised shelters and, in some
  cases, administrative support and other structures. This is a preliminary analysis
  and has not yet been validated in the field. Please send ground feedback to UNITAR
  / UNOSAT.. [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-rubkona-base-rubkona-south-sudan-january-09-2014]'
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
    description: Internally displaced persons (IDPs) sheltering in UNMISS Rubkona
      base compound
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
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts reviewed WorldView-2 satellite imagery acquired on
    2 January 2014 and compared multi-temporal images to identify and delineate areas
    occupied by IDPs within the UNMISS Rubkona base. Satellite-detected shelter structures
    and administrative areas were mapped as polygon features with confidence and validation
    metadata.
  sources:
  - id: source_1
    license: null
    name: United Nations Satellite Centre (UNOSAT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/geodata-of-idp-camp-in-unmiss-rubkona-base-rubkona-south-sudan-january-09-2014
  rel: source
loss:
  losses:
  - asset_category: population
    asset_dimension: population
    description: Displaced population (IDPs) fleeing violence in South Sudan conflict
    disaster_identifiers: []
    hazard:
      classification: null
      id: hazard_convective_storm
      intensity_measure: sws_10m:m/s
      process: null
      trigger: null
      type: convective_storm
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
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Camp in UNMISS Rubkona Base, Rubkona, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_8f76699f
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_shp.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of IDP Camp in UNMISS Rubkona Base, Rubkona, South Sudan (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_d075103e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-ssd_unosat_geodataidpcampunmissrubko_20140109
spatial:
  bbox: null
  centroid: null
  countries:
  - SSD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2014-01-09'
temporal_resolution: null
title: Geodata of IDP Camp in UNMISS Rubkona Base, Rubkona, South Sudan
version: null
vulnerability: null
---
