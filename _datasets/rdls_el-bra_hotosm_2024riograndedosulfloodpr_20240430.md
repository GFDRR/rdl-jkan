---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/2024-rio-grande-do-sul-flood-pre-disaster-buildings-openstreetmap
creator:
  affiliation: null
  email: null
  name: Humanitarian OpenStreetMap Team (HOT)
  url: https://data.humdata.org/dataset/2024-rio-grande-do-sul-flood-pre-disaster-buildings-openstreetmap
dataset_id: rdls_el-bra_hotosm_2024riograndedosulfloodpr_20240430
description: 'Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This
  dataset contains buildings and destroyed buildings mapped as part of the HOTOSM
  Rio Grande do Sul Floods Activation mapping project.. [Source: This metadata record
  was automatically extracted from the Humanitarian Data Exchange (HDX); Original
  dataset: https://data.humdata.org/dataset/2024-rio-grande-do-sul-flood-pre-disaster-buildings-openstreetmap]'
details: null
exposure:
- asset_type:
    description: Building footprints and attributes mapped before the May 2024 Rio
      Grande do Sul floods across five municipalities
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
license: ODbL-1.0/
lineage:
  description: Building geometries and attributes were collaboratively mapped on OpenStreetMap
    through the HOT Tasking Manager platform by local and remote volunteers as part
    of the Rio Grande do Sul Floods Activation mapping project. The dataset captures
    pre-disaster building stock across five municipalities (Encantado, Arroio do Meio,
    Roca Sales, Mucum, Cruzeiro do Sul) with OSM feature tags including structural
    attributes (building type, levels, height) and facility classifications (healthcare,
    amenity, shop, industrial).
  sources:
  - id: source_1
    license: null
    name: Humanitarian OpenStreetMap Team (HOT)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/2024-rio-grande-do-sul-flood-pre-disaster-buildings-openstreetmap
  rel: source
loss:
  losses:
  - asset_category: buildings
    asset_dimension: structure
    description: Buildings destroyed or damaged by the May 2024 Rio Grande do Sul
      floods
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
  description: Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This
    dataset contains buildings and destroyed buildings mapped as part of the HOTOSM
    Rio Grande do Sul Floods Activation mapping project. It includes buildings located
    in the municipality of Encantado.
  download_url: https://data.humdata.org/dataset/51897dd0-dc3c-41a3-bddc-2e94bc0678a7/resource/76e27050-d7e5-46fd-984b-eb748d9f582a/download/br-rs-encantado-edificacoes_osm.geojson
  format: null
  id: resource_76e27050
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BR-RS-Encantado-Edificacoes_OSM.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This
    dataset contains buildings and destroyed buildings mapped as part of the HOTOSM
    Rio Grande do Sul Floods Activation mapping project. It includes buildings located
    in the municipality of Arroio do Meio.
  download_url: https://data.humdata.org/dataset/51897dd0-dc3c-41a3-bddc-2e94bc0678a7/resource/fef99a87-df90-460b-aac6-649bcbeabc86/download/br-rs-arroio_do_meio-edificacoes_osm.geojson
  format: null
  id: resource_fef99a87
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BR-RS-Arroio_do_Meio-Edificacoes_OSM.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This
    dataset contains buildings and destroyed buildings mapped as part of the HOTOSM
    Rio Grande do Sul Floods Activation mapping project. It includes buildings located
    in the municipality of Roca Sales.
  download_url: https://data.humdata.org/dataset/51897dd0-dc3c-41a3-bddc-2e94bc0678a7/resource/68b24776-5d16-4416-9f06-a1927fbb015f/download/br-rs-roca_sales-edificacoes_osm.geojson
  format: null
  id: resource_68b24776
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BR-RS-Roca_Sales-Edificacoes_OSM.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This\
    \ dataset contains buildings and destroyed buildings mapped as part of the HOTOSM\
    \ Rio Grande do Sul Floods Activation mapping project. It includes buildings located\
    \ in the municipality of Mu\u221A\xDFum."
  download_url: https://data.humdata.org/dataset/51897dd0-dc3c-41a3-bddc-2e94bc0678a7/resource/71091013-6e2f-4444-86fe-2dd103f1e06a/download/br-rs-mucum-edificacoes_osm.geojson
  format: null
  id: resource_71091013
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BR-RS-Mucum-Edificacoes_OSM.geojson
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Buildings Existing Before the May 2024 Rio Grande do Sul Floods. This
    dataset contains buildings and destroyed buildings mapped as part of the HOTOSM
    Rio Grande do Sul Floods Activation mapping project. It includes buildings located
    in the municipality of Cruzeiro do Sul.
  download_url: https://data.humdata.org/dataset/51897dd0-dc3c-41a3-bddc-2e94bc0678a7/resource/ce2f7e44-c469-423c-bc50-1d4818f330a8/download/br-rs-cruzeiro_do_sul-edificacoes_osm.geojson
  format: null
  id: resource_ce2f7e44
  media_type: application/geo+json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: BR-RS-Cruzeiro_do_Sul-Edificacoes_OSM.geojson
risk_data_type:
- exposure
- loss
schema: rdls-10
slug: rdls_el-bra_hotosm_2024riograndedosulfloodpr_20240430
spatial:
  bbox: null
  centroid: null
  countries:
  - BRA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2024-04-30'
temporal_resolution: null
title: 'Brazil : 2024 Rio Grande do Sul Flood Pre-Disaster Buildings by Municipality
  (OpenStreetMap Export)'
version: null
vulnerability: null
---
