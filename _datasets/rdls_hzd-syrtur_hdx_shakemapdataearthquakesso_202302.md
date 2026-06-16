---
attributions:
- entity:
    affiliation: null
    email: null
    name: United States Geological Survey (USGS)
    url: https://data.humdata.org/dataset/earthquake-in-southeastern-turkiye-and-northwestern-syria
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: HDX
  url: https://data.humdata.org/dataset/earthquake-in-southeastern-turkiye-and-northwestern-syria
creator:
  affiliation: null
  email: null
  name: United States Geological Survey (USGS)
  url: https://data.humdata.org/dataset/earthquake-in-southeastern-turkiye-and-northwestern-syria
dataset_id: rdls_hzd-syrtur_hdx_shakemapdataearthquakesso_202302
description: "On 6 February 2023 at 4:17h, local time in T\xFCrkiye (01:17 GMT), an\
  \ earthquake with a magnitude of 7.8 hit T\xFCrkiye and northwestern Syria. It mainly\
  \ affected the cities of Adana, Adiyaman, Diyarbakir, Gaziantep, Hatay, Kahramanmaras,\
  \ Kilis, Malatya, Osmaniye, and Sanliurfa in southeastern T\xFCrkiye and Aleppo,\
  \ Hama, Idlib, Lattakie, and Tartous governorates in northwestern Syria. The earthquake's\
  \ epicentre was 23km east of the district of Nurdagi, in T\xFCrkiye's Gaziantep\
  \ city, at a depth of 24.1km. T\xFCrkiye is vulnerable to earthquakes because it\
  \ lies on several fault lines, and the 7.8 quake seems to be the strongest since\
  \ 1939 On the same day, at 13:45h, local time in T\xFCrkiye, another earthquake\
  \ with a magnitude of 7.6 struck T\xFCrkiye. It hit four kilometres southeast of\
  \ Ekinozu town in Kahraman Maras province, where the 7.8 earthquake hit hours earlier.\
  \ As at 6 February, there had been at least 78 aftershocks.. [Source: This metadata\
  \ record was automatically extracted from the Humanitarian Data Exchange (HDX);\
  \ Original dataset: https://data.humdata.org/dataset/earthquake-in-southeastern-turkiye-and-northwestern-syria]"
details: 'Glide: EQ-2023-000015-TUR'
exposure: []
hazard:
  event_sets:
  - analysis_type: deterministic
    calculation_method: simulated
    event_count: 0
    events: []
    frequency_distribution: null
    hazards:
    - classification: null
      id: hazard_1
      intensity_measure: PGA:g
      process: ground_motion
      trigger: null
      type: earthquake
    id: event_set_1
    occurrence_range: null
    seasonality: null
license: CC-BY-4.0
lineage:
  description: "USGS ShakeMap methodology automatically processed instrumental seismic\
    \ data from the 6 February 2023 earthquakes (M7.8 Pazarcik and M7.5 Elbistan)\
    \ combined with local geology and earthquake parameters to generate deterministic\
    \ ground motion intensity grids. Results are distributed as polygon shapefiles\
    \ and JSON representations of peak ground acceleration (PGA) and other intensity\
    \ measures across affected regions in T\xFCrkiye and Syria."
  sources:
  - id: source_1
    license: null
    name: United States Geological Survey (USGS)
    risk_data_type:
    - hazard
    type: model
    url: null
    used_in: hazard
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/earthquake-in-southeastern-turkiye-and-northwestern-syria
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: http://earthquake.usgs.gov/shakemap
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Zipped shapefile archive containing all ShakeMap data from the 6 February\
    \ 2023 M 7.8 earthquake over Central T\xFCrkiye. Extracted from USGS Earthquake\
    \ Hazard Program event page for the earthquake"
  download_url: https://data.humdata.org/dataset/50d93259-2d49-4f84-85e6-3cd0aa03dfaa/resource/065bd879-34c2-42ea-96eb-eb8736a6fd44/download/m-7.8-pazarcik-earthquake-kahramanmaras-earthquake-sequence.zip
  format: null
  id: resource_065bd879
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: M 7.8 - Pazarcik earthquake, Kahramanmaras earthquake sequence.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Contours of macroseismic intensity. Extracted from USGS Earthquake
    Hazard Program event page for the earthquake
  download_url: https://data.humdata.org/dataset/50d93259-2d49-4f84-85e6-3cd0aa03dfaa/resource/eaa64ce6-8737-408d-8e51-672a5debeee0/download/m-7.8-pazarcik-earthquake-kahramanmaras-earthquake-sequence.json
  format: null
  id: resource_eaa64ce6
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: M 7.8 - Pazarcik earthquake, Kahramanmaras earthquake sequence.json
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Zipped shapefile archive containing all ShakeMap data from the 6 February\
    \ 2023 M 7.8 earthquake 4km SSE of Ekin\xF6z\xFC, T\xFCrkiye. Extracted from USGS\
    \ Earthquake Hazard Program event page for the earthquake"
  download_url: https://data.humdata.org/dataset/50d93259-2d49-4f84-85e6-3cd0aa03dfaa/resource/05c40fec-4f50-4801-bab5-164eb97dc704/download/m-7.5-elbistan-earthquake-kahramanmaras-earthquake-sequence.zip
  format: null
  id: resource_05c40fec
  media_type: application/vnd.shp
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: M 7.5 - Elbistan earthquake Kahramanmaras earthquake sequence.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Contours of macroseismic intensity. Extracted from USGS Earthquake
    Hazard Program event page for the earthquake
  download_url: https://data.humdata.org/dataset/50d93259-2d49-4f84-85e6-3cd0aa03dfaa/resource/f7663c38-3a5f-45c8-9566-d4e57b3a8664/download/m-7.5-elbistan-earthquake-kahramanmaras-earthquake-sequence.json
  format: null
  id: resource_f7663c38
  media_type: application/json
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: M 7.5 - Elbistan earthquake Kahramanmaras earthquake sequence.json
risk_data_type:
- hazard
schema: rdls-10
slug: rdls_hzd-syrtur_hdx_shakemapdataearthquakesso_202302
spatial:
  bbox: null
  centroid: null
  countries:
  - SYR
  - TUR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2023-02-07'
  start: '2023-02-06'
temporal_resolution: null
title: "ShakeMap Data for the Earthquakes in Southeastern T\xFCrkiye and Northwestern\
  \ Syria"
version: null
vulnerability: null
---
