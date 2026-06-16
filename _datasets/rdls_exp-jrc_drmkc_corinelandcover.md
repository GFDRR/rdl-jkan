---
attributions:
- entity:
    affiliation: null
    email: null
    name: European Commision (EC)
    url: https://commission.europa.eu/
  id: Entity_1
  role: owner
- entity:
    affiliation: null
    email: copernicus@eea.europa.eu
    name: Copernicus Land Monitoring Service
    url: https://land.copernicus.eu/
  id: Entity_2
  role: custodian
- entity:
    affiliation: null
    email: sdi@eea.europa.eu
    name: European Environment Agency
    url: http://www.eea.europa.eu/
  id: Entity_3
  role: resource_provider
catalog: null
contact_point:
  affiliation: null
  email: copernicus@eea.europa.eu
  name: Copernicus Land Monitoring Service helpdesk
  url: https://land.copernicus.eu/en/contact-service-helpdesk
creator:
  affiliation: null
  email: copernicus@eea.europa.eu
  name: Copernicus Land Monitoring Service
  url: https://land.copernicus.eu/
dataset_id: rdls_exp-jrc_drmkc_corinelandcover
description: Corine land cover for the 2018 reference year
details: Provides pan-European CORINE Land Cover inventory for 44 thematic classes
  for the 2018 reference year. The dataset has a Minimum Mapping Unit (MMU) of 25
  hectares (ha) for areal phenomena and a Minimum Mapping Width (MMW) of 100 m for
  linear phenomena and is available as vector and as 100 m raster data.
exposure:
- asset_type: null
  category: natural_environment
  id: exp_1
  metrics:
  - dimension: content
    id: landcover
    measurement:
      quantity_kind: area
      unit: null
hazard: null
license: CC-BY-4.0
lineage:
  description: null
  sources:
  - id: Source_1
    license: null
    name: European Environment Agency
    risk_data_type: null
    type: dataset
    url: https://sdi.eea.europa.eu/catalogue/copernicus/api/records/960998c1-1870-4e82-8051-6485205ebbac?language=all
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
loss: null
project:
  name: Copernicus Land Monitoring Service
  url: https://land.copernicus.eu/
publisher:
  affiliation: null
  email: sdi@eea.europa.eu
  name: European Environment Agency
  url: http://www.eea.europa.eu/
purpose: To provide consistent and thematically detailed land cover and land use information
  across Europe for environmental monitoring, ecosystem protection, climate change
  tracking, and supporting EU environmental policy implementation.
referenced_by:
- author_names: null
  date_published: '2020-01-01'
  doi: https://doi.org/10.2909/960998c1-1870-4e82-8051-6485205ebbac
  id: Ref_1
  name: European Union, Copernicus Land Monitoring Service, European Environment Agency
    (EEA)
  url: https://sdi.eea.europa.eu/catalogue/copernicus/api/records/960998c1-1870-4e82-8051-6485205ebbac?language=all
resources:
- access_url: https://land.copernicus.eu/en/products/corine-land-cover/clc2018
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:3035
  description: CORINE Land Cover 2018, Europe (Corine land cover for the 2018 reference
    year)
  download_url: https://eea.github.io/clms-api-docs/download.html#download-prepackaged-files
  format: null
  id: CORINE_Landcover_2018
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: 100
  temporal:
    central_year: null
    duration: null
    end: '2018-12-31'
    start: '2017-01-01'
  temporal_resolution: null
  title: CORINE Land Cover 2018
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-jrc_drmkc_corinelandcover
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  - BEL
  - BGR
  - HRV
  - CYP
  - CZE
  - DNK
  - EST
  - FIN
  - FRA
  - DEU
  - GRC
  - HUN
  - IRL
  - ITA
  - LVA
  - LTU
  - LUX
  - MLT
  - NLD
  - POL
  - PRT
  - ROU
  - SVK
  - SVN
  - ESP
  - SWE
  gazetteer_entries:
  - description: Europe
    id: Location_1
    scheme: GEONAMES
    uri: https://www.geonames.org/6255148/europe.html
  - description: EEA39
    id: Location_2
    scheme: NUTS
    uri: https://sdi.eea.europa.eu/catalogue/srv/api/records/8526ff78-b000-42e1-8360-a2fb3a51e4ac
  scale: regional
spatial_resolution: null
temporal: null
temporal_resolution: null
title: CORINE Land Cover 2018, Europe
version: V2020_20u1
vulnerability: null
---
