---
attributions:
- entity:
    affiliation: null
    email: null
    name: SPC Statistics for Development Division (SDD)
    url: https://data.humdata.org/dataset/pdh-vanuatu_population_grid_2020
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-vanuatu_population_grid_2020
creator:
  affiliation: null
  email: null
  name: Pacific Community
  url: https://data.humdata.org/dataset/pdh-vanuatu_population_grid_2020
dataset_id: rdls_exp-vut_spc_vanuatupopulationgrid2020_20200403
description: 'Population Raster Vanuatu 2020 Data Input: Household locations from
  2016 Population and Housing Census conducted using Survey Solutions CAPI (Computer
  Assisted Personal Interview). Year Population Growth Rate of 2.3% has been applied
  to update population up to 2020 Household locations vector layer has been transformed
  into a 100m resolution raster. Access this dataset from the Pacific Data Hub. [Source:
  This metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/pdh-vanuatu_population_grid_2020]'
details: null
exposure:
- asset_type:
    description: Gridded population distribution at 100m resolution derived from 2016
      census household locations and projected to 2020 using 2.3% annual growth rate
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
  description: Household locations from the 2016 Vanuatu Population and Housing Census
    (collected via CAPI survey) were transformed into a 100m resolution raster grid.
    Population counts were projected to 2020 by applying a 2.3% annual growth rate
    to account for demographic change between census and target year.
  sources:
  - id: source_1
    license: null
    name: SPC Statistics for Development Division (SDD)
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/pdh-vanuatu_population_grid_2020
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: Census
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Population Raster Vanuatu 2020 HH locations vector layer transformed
    into a 100m resolution raster. This is a demo version, SDD is still evaluating
    the methodology but given the COVID outbreak the dataset has been early released.
  download_url: https://pacificdata.org/data/dataset/1cb668eb-e915-4970-8b87-89aead626d39/resource/08748669-bfb9-404a-9ca4-bd1b49f337ef/download/rastpop2020rps_100m.tif
  format: null
  id: resource_3c089412
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT_Pop_Grid_2020
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu_Population_Grid_2020 (Text)
  download_url: https://pacificdata.org/data/dataset/1cb668eb-e915-4970-8b87-89aead626d39/resource/4dc1ace6-b011-44f9-8262-6e4b7a0cd698/download/vut_popgrid_2020_readme.txt
  format: null
  id: resource_049e84bb
  media_type: text/plain
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT_PopGrid_2020_README
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu_Population_Grid_2020 (Static maps of the Vanuatu Population
    Grid 2020)
  download_url: https://pacificdata.org/data/dataset/1cb668eb-e915-4970-8b87-89aead626d39/resource/c0737a05-4e52-41f7-bfbb-be8077468542/download/vut_popgrid_atlas.zip
  format: zip
  id: resource_a30ba26a
  media_type: null
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT_PopGrid_2020_Atlas
- access_url: https://tiles.arcgis.com/tiles/OAxZXfmfGWlgx9kD/arcgis/rest/services/Van_PPG_MS/MapServer
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Vanuatu_Population_Grid_2020 (VUT_PopGrid_2020_Web Mapping Service)
  download_url: null
  format: null
  id: resource_1e7c1ab6
  media_type: text/html
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: VUT_PopGrid_2020_Web Mapping Service
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-vut_spc_vanuatupopulationgrid2020_20200403
spatial:
  bbox: null
  centroid: null
  countries:
  - VUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: null
  start: '2020-04-03'
temporal_resolution: null
title: Vanuatu_Population_Grid_2020
version: null
vulnerability: null
---
