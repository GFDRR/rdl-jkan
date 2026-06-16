---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
creator:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
dataset_id: rdls_vln-coclico_cba
description: 'Cost-benefit Analysis of Coastal Adaptation identifies the most cost-effective
  adaptation strategies - protection, retreat, or accommodation - to manage coastal
  flood risks under different climate scenarios, with insights available at both national
  and local levels. Spatial Coverage: Coastal NUTS0 (country level) Sources: regional
  sea level projections, vertical land motion, adaptation costs and protection levels,
  extreme return periods from COAST-RP, and coastal floodplain profiles from Copernicus
  DEM and Global Human Settlement data. Common usage: Decision-making for coastal
  resilience, adaptation strategy evaluation. More Info about the dataset: User Handbook.
  Variants in the source dataset - adaptation strategy: protection (Protect), retreat
  (Retreat), acc (Accommodate), protect_retreat (Protect & Retreat), no_adaptation
  (No Adaptation) - The adaptation strategy related to raising coastal defenses (protection),
  managed withdrawal from vulnerable areas (retreat), a combination of these strategies
  (protect & retreat), implementing flood-proofing measures (accommodation) or areas
  where adaptation measure are deemed inefficient (no adaptation); scenarios: SSP126
  (SSP1-2.6), SSP245 (SSP2-4.5), SSP585 (SSP5-8.5) - Climate scenarios based on IPCC''s
  Shared Socioeconomic Pathways (SSPs). High-end (if applicable) refers to P83 of
  SSP5-8.5, taking into account low-confidence processes. Other scenarios use the
  P50; time: 2050, 2100, 2150 - Time slice applied to the data. Either present-day
  (2010) or future state representing medium (2030 till 2050) and long term (2050
  till 2100) outlook. [Source: This metadata record was automatically extracted from
  the STAC catalog coclico (https://www.openearth.nl/coclico-workbench/data_catalog/)]'
details: null
exposure: []
hazard: null
license: https://spdx.org/licenses/CC-BY-4.0.html
lineage:
  description: 'Cost-benefit Analysis of Coastal Adaptation identifies the most cost-effective
    adaptation strategies - protection, retreat, or accommodation - to manage coastal
    flood risks under different climate scenarios, with insights available at both
    national and local levels. Spatial Coverage: Coastal NUTS0 (country level) Sources:
    regional sea level projections, vertical land motion, adaptation costs and protection
    levels, extreme return periods from COAST-RP, and coastal floodplain profiles
    from Copernicus DEM and Global Human Settlement data. Common usage: Decision-making
    for coastal resilience, adaptation strategy evaluation. More Info about the dataset:
    User Handbook'
  sources:
  - id: source_1
    license: null
    name: Global Climate Forum
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://globalclimateforum.org/
    used_in: vulnerability
  - id: source_2
    license: null
    name: Deltares
    risk_data_type:
    - vulnerability
    type: dataset
    url: https://deltares.nl
    used_in: vulnerability
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Global Climate Forum
  url: https://globalclimateforum.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: ref_citation
  name: "V\xC3\xB6lz, V., Lincke, D., Hinkel, J., Honsel, L. (2024). Efficient adaptation\
    \ pathways for European floodplains. tbd"
  url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cba/collection.json
resources:
- access_url: https://storage.googleapis.com/coclico-data-public/coclico/coclico-stac/cba/collection.json
  baseline_period: null
  climate: null
  conforms_to: https://api.stacspec.org/v1.0.0/
  coordinate_system: null
  description: Source STAC Collection metadata for this dataset, hosted as part of
    the CoCliCo catalog. Conforms to STAC v1.0.0.
  download_url: null
  format: null
  id: resource_stac_collection
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'STAC Collection: CoCliCo - Cost Benefit Analysis [cba]'
- access_url: https://storage.googleapis.com/download/storage/v1/b/coclico-data-public/o/coclico%2Fassets%2Fthumbnails%2Fcba.png?alt=media
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost Benefit Analysis
  download_url: null
  format: null
  id: resource_thumbnail
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Thumbnail
- access_url: https://coclico.avi.deltares.nl/geoserver/gwc/service/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&LAYER=cba:GCF_open_CBA_country_all_EPSG3035&STYLE=&TILEMATRIX=EPSG:900913:{z}&TILEMATRIXSET=EPSG:900913&FORMAT=application/vnd.mapbox-vector-tile&TILECOL={x}&TILEROW={y}
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost Benefit Analysis (Geoserver Parquet link)
  download_url: null
  format: null
  id: resource_geoserverlink
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: Geoserver Parquet link
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: CoCliCo - Cost Benefit Analysis (Snapshot of the collection's STAC
    items exported to GeoParquet format.)
  download_url: https://storage.googleapis.com/coclico-data-public/coclico/CBA_stats/GCF.open.CBA_country.all.parquet
  format: null
  id: resource_geoparquetstacitems
  media_type: application/vnd.apache.parquet
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoParquet STAC items
risk_data_type:
- vulnerability
schema: rdls-10
slug: rdls_vln-coclico_cba
spatial:
  bbox:
  - -90.23528381409483
  - -29.857082115784582
  - 103.456913582018
  - 39.79889221318682
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020'
  start: '2020'
temporal_resolution: null
title: CoCliCo - Cost Benefit Analysis
version: null
vulnerability: null
---
