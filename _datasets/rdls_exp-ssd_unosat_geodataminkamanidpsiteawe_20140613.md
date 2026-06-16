---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-june-13-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-june-13-2014
dataset_id: rdls_exp-ssd_unosat_geodataminkamanidpsiteawe_20140613
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Minkaman IDP Site in Lakes State, South Sudan, as seen by the WorldView-1
  satellite on 10 May 2014. People displaced by ongoing instability in the region
  of Bor have established multiple IDP camps on the west bank of the White Nile in
  Awerial County. This site at Minkaman occupies multiple areas along the White Nile,
  and includes approximately 9,391 shelters and 450 infrastructure or support buildings.
  Note that IDPs sheltering under trees are not detected by this analysis. This is
  a preliminary analysis and has not yet been validated in the field. Please send
  ground feedback to UNITAR / UNOSAT. [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-june-13-2014]'
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
    description: Satellite-detected shelters and support buildings at Minkaman IDP
      site, classified by structure type and validation status
    id: buildings
    scheme: null
    title: null
    uri: null
  category: buildings
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: CC-BY-4.0
lineage:
  description: UNOSAT analysts reviewed WorldView-1 satellite imagery acquired on
    10 May 2014 and manually identified shelter and building structures at the Minkaman
    IDP site in Awerial County through visual interpretation and comparison with reference
    imagery. Detected features were classified by type (shelter vs. infrastructure),
    confidence level, and validation status, resulting in a spatial inventory of approximately
    9,391 shelters and 450 support buildings.
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
- href: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-june-13-2014
  rel: source
loss: null
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
  description: Geodata of Minkaman IDP site, Awerial County, Lakes State, South Sudan
    (Shapefile)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/IDP_Minkaman_Shelters_10May2014.zip
  format: null
  id: resource_1b85cd1e
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: IDP_Minkaman_Shelters_10May2014.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Geodata of Minkaman IDP site, Awerial County, Lakes State, South Sudan
    (Geodatabase)
  download_url: https://unosat-maps.web.cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_Minkaman_10May2014_.gdb.zip
  format: Geodatabase
  id: resource_228b106d
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD_Minkaman_10May2014_.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodataminkamanidpsiteawe_20140613
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
  start: '2014-06-13'
temporal_resolution: null
title: Geodata of Minkaman IDP site, Awerial County, Lakes State, South Sudan
version: null
vulnerability: null
---
