---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
creator:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net/api/v2/users/1001
dataset_id: rdls_exp-som_icpac_livelihoodzones
description: 'Livelihood zones - Anthromes (Anthropogenic Biomes) represent the globally
  significant patterns of Earth''s ecology created and sustained by human populations
  and their use of land, including Intensive anthromes (dense settlements, villages,
  croplands, and rangelands), Cultured anthromes (low intensity use woodlands and
  drylands), and Wildlands without evidence of human populations or land use. These
  maps illustrate human cultural transformation and use of the terrestrial biosphere
  over the past 12,000 years at 60 time points between 10,000 BCE and 2017 CE, at
  the scale of regional landscapes (~100 km2), using a Discrete Global Grid system
  (DGG) that divides Earth''s land into 1,429,024 equal area hexagons. [Source: This
  metadata record was automatically extracted from the GeoNode portal icpac]'
details: Processing Guide Download the Anthromes-12k-DGG shapefile from Anthromes
  12K DGG (V1) Full Dataset - Anthromes 12K DGG Dataverse. Load the file in your QGIS
  and export the id and 2017AD columns to a csv. Re-rank the anthromes in the 2017AD
  column for each id based on your thematic expertise analysis (as suggested in the
  sample ranking above). Export your results into a new CSV, do a join with the shapefile,
  and map based on the new ranking.
exposure:
- asset_type: null
  category: natural_environment
  id: exposure_1
  metrics:
  - dimension: structure
    id: metric_1
    measurement:
      quantity_kind: area
      unit: null
- asset_type: null
  category: economic_indicator
  id: exposure_2
  metrics:
  - dimension: index
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: null
  sources:
  - id: source_1
    license: null
    name: IGAD DRM Team
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://geoportal.icpac.net/layers/som_Livelihood_zones1_normalized:geonode:som_Livelihood_zones1_normalized
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: IGAD DRM Team
  url: https://geoportal.icpac.net
purpose: null
referenced_by: []
resources:
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:som_Livelihood_zones1_normalized
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Somalia Livelihood Zones (OGC WMS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:som_Livelihood_zones1_normalized&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://geoportal.icpac.net/datasets/geonode:geonode:som_Livelihood_zones1_normalized
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Somalia Livelihood Zones (OGC WCS: geonode Service)'
  download_url: https://geoportal.icpac.net/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:som_Livelihood_zones1_normalized
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_icpac_livelihoodzones
spatial:
  bbox:
  - 40.976011762
  - -1.686411878
  - 51.426011762
  - 12.013588122
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Somalia Livelihood Zones
version: null
vulnerability: null
---
