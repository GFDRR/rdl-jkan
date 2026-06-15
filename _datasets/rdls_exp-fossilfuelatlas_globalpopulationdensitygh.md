---
attributions: []
catalog: null
contact_point:
  affiliation: null
  email: noah.rarick@gmail.com
  name: noahrarick
  url: https://www.fossilfuelatlasportal.org/api/v2/users/1028
creator:
  affiliation: null
  email: noah.rarick@gmail.com
  name: noahrarick
  url: https://www.fossilfuelatlasportal.org/api/v2/users/1028
dataset_id: rdls_exp-fossilfuelatlas_globalpopulationdensitygh
description: 'Global Population Density via the US Greenhouse Gas Center backed by
  NASA. This tiff displays population density in 2020 as estimated by the GGC. https://earth.gov/ghgcenter
  https://data.ghg.center/browseui/index.html#sedac-popdensity-yeargrid5yr-v4.11/
  [Source: This metadata record was automatically extracted from the GeoNode portal
  fossilfuelatlas]'
details: null
exposure:
- asset_type: null
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
  description: null
  sources:
  - id: source_1
    license: null
    name: noahrarick
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://www.fossilfuelatlasportal.org/catalogue/#/dataset/744
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: noahrarick
  url: https://www.fossilfuelatlasportal.org
purpose: null
referenced_by: []
resources:
- access_url: https://www.fossilfuelatlasportal.org/datasets/geonode:geonode:gpw_v4_population_density_2020_cog
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wms
  coordinate_system: EPSG:4326
  description: 'Global Population Density (GHG) (OGC WMS: geonode Service)'
  download_url: https://www.fossilfuelatlasportal.org/geoserver/ows?service=WMS&version=1.1.1&request=GetMap&layers=geonode:geonode:gpw_v4_population_density_2020_cog&format=image%2Fpng
  format: null
  id: resource_0
  media_type: image/png
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WMS: geonode Service'
- access_url: https://www.fossilfuelatlasportal.org/datasets/geonode:geonode:gpw_v4_population_density_2020_cog
  baseline_period: null
  climate: null
  conforms_to: http://www.opengis.net/def/serviceType/ogc/wcs
  coordinate_system: EPSG:4326
  description: 'Global Population Density (GHG) (OGC WCS: geonode Service)'
  download_url: https://www.fossilfuelatlasportal.org/geoserver/ows?service=WCS&version=2.0.1&request=DescribeCoverage&CoverageId=geonode__geonode:gpw_v4_population_density_2020_cog
  format: null
  id: resource_1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: 'OGC WCS: geonode Service'
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Population Density (GHG)
  download_url: https://www.fossilfuelatlasportal.org/geoserver/ows?service=WCS&request=GetCoverage&coverageid=geonode__gpw_v4_population_density_2020_cog&format=image%2Ftiff&version=2.0.1&compression=DEFLATE&tileWidth=512&tileHeight=512
  format: null
  id: resource_2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: GeoTIFF
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: EPSG:4326
  description: Global Population Density (GHG)
  download_url: https://www.fossilfuelatlasportal.org/api/v2/assets/480/link
  format: null
  id: resource_3
  media_type: image/tiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gpw_v4_population_density_2020_cog
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-fossilfuelatlas_globalpopulationdensitygh
spatial:
  bbox:
  - -180.0
  - -90.0
  - 179.99999999999983
  - 90.0
  centroid: null
  countries:
  - GLO
  gazetteer_entries: []
  scale: global
spatial_resolution: null
temporal:
  central_year: 2025
  duration: null
  end: null
  start: null
temporal_resolution: null
title: Global Population Density (GHG)
version: null
vulnerability: null
---
