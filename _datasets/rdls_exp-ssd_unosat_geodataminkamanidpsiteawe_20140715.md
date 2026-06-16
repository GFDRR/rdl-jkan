---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-july-15-2014
creator:
  affiliation: null
  email: null
  name: United Nations Satellite Centre (UNOSAT)
  url: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-july-15-2014
dataset_id: rdls_exp-ssd_unosat_geodataminkamanidpsiteawe_20140715
description: 'This map illustrates satellite-detected shelters and other buildings
  at the Minkaman IDP Site in Lakes State, South Sudan, as seen by the WorldView-2
  satellite on 3 July 2014. People displaced by ongoing instability in the region
  of Bor have established multiple IDP camps on the west bank of the White Nile in
  Awerial County. Imagery acquired on 10 May 2014 showed approximately 9,391 shelters
  and 450 infrastructure or support buildings occupying multiple areas along the White
  Nile. Imagery also showed an area being prepared for accommodating new shelters.
  As of 3 July 2014 this ground has been partially covered by shelters as well as
  other areas of the IDP site, and approximately 13,492 shelters and 572 infrastructure
  or support buildings have been detected. Note that IDPs sheltering under trees are
  not detected by this analysis. This is a preliminary analysis and has not yet been
  validated in the field. Please send ground feedback to UNITAR / UNOSAT. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-july-15-2014]'
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
    description: Satellite-detected shelter and building structures at Minkaman IDP
      site, classified by type (shelters vs. infrastructure/support buildings)
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
- asset_type:
    description: Displaced population residing in IDP shelters at Minkaman site
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_2
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: UNOSAT analysts manually reviewed and compared WorldView-2 satellite
    imagery acquired on 10 May 2014 and 3 July 2014 to detect shelter and infrastructure
    structures at Minkaman IDP site through visual interpretation and change detection.
    Building footprints were digitized and attributed with confidence levels and validation
    status to create a spatial inventory of displaced population assets.
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
- href: https://data.humdata.org/dataset/geodata-of-minkaman-idp-site-awerial-county-lakes-state-south-sudan-july-15-2014
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
  description: Geodata of Minkaman IDP Site, Awerial County, Lakes State, South Sudan
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD_shp.zip
  format: null
  id: resource_07da274b
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
  description: Geodata of Minkaman IDP Site, Awerial County, Lakes State, South Sudan
    (Shapefile)
  download_url: https://cern.ch/unosat-maps/SS/CE20131218SSD/CE20131218SSD.gdb.zip
  format: null
  id: resource_200d8382
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: CE20131218SSD.gdb.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ssd_unosat_geodataminkamanidpsiteawe_20140715
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
  start: '2014-07-15'
temporal_resolution: null
title: Geodata of Minkaman IDP Site, Awerial County, Lakes State, South Sudan
version: null
vulnerability: null
---
